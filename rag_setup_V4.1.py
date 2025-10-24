# rag_setup_V4.py - Enhanced RAG with Equipment Metadata & Configurable Image Processing
"""
🔧 EQUIPMENT-AWARE RAG SYSTEM V4 with IMAGE SUPPORT

📸 TO ENABLE IMAGE PROCESSING:
1. Set ENABLE_IMAGE_PROCESSING = True in VectorStoreConfig class
2. Set GENERATE_PAGE_IMAGES = True to save full page images  
3. Set GENERATE_PICTURE_IMAGES = True to save individual image crops
4. Set ENABLE_IMAGE_DESCRIPTIONS = True for AI image captions (requires API)
5. Adjust IMAGE_SCALE (1-3) for quality vs speed

⚠️ WARNING: Image processing significantly increases processing time and storage!
Current default: Images DISABLED for fast processing

📁 Image Storage Locations:
- Page images: output/markdowns/{filename}_artifacts/
- Individual images: output/markdowns/{filename}_artifacts/pictures/
- Image references: Embedded in markdown files
"""

import os
import re
import json
import pickle
from pathlib import Path
from dotenv import load_dotenv
import tiktoken
from datetime import datetime
from typing import List, Dict, Any, Optional, Literal

from config import (
    PDF_FOLDER, MARKDOWN_DIR, CHUNKS_DIR, CHROMA_DB_DIR, 
    EMBEDDING_MODEL, EMBEDDING_DIMENSION, EMBEDDING_BATCH_SIZE,
    FAISS_INDEX_PATH, FAISS_METADATA_PATH, FAISS_JSON_PATH,
    VECTOR_STORE_TYPE, FAISS_INDEX_TYPE, MAX_TOKENS_PER_CHUNK, CHUNK_OVERLAP
)
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    PictureDescriptionApiOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.types.doc.document import ImageRefMode

import chromadb
from chromadb.utils import embedding_functions

# FAISS imports
try:
    import faiss
    import numpy as np
    FAISS_AVAILABLE = True
except ImportError:
    FAISS_AVAILABLE = False
    print("⚠️ FAISS not installed. Install with: pip install faiss-cpu (or faiss-gpu)")

# Updated deprecated import
try:
    from langchain_openai import OpenAIEmbeddings  # modern location
except ImportError:  # fallback for older envs
    from langchain.embeddings.openai import OpenAIEmbeddings  # type: ignore

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

# =================================
# 🏭 Equipment Metadata Extraction
# =================================
def extract_equipment_metadata(filename: str, content: str = "") -> Dict[str, str]:
    """
    Extract equipment type, make, and model from filename and content.
    This function analyzes PDF filenames and content to identify equipment details.
    """
    filename_lower = filename.lower()
    content_lower = content.lower()
    
    # Default values
    equipment_type = "Unknown"
    make = "Unknown"  
    model = "Unknown"
    
    # Equipment Type Detection (based on common keywords)
    equipment_patterns = {
        "flow_meter": ["flow", "meter", "flowmeter"],
        "pump": ["pump", "flygt", "submersible"],
        "control_system": ["control", "automatic", "plc", "scada"],
        "compressor": ["compressor", "air", "pneumatic"],
        "valve": ["valve", "gate", "ball", "check"],
        "sensor": ["sensor", "pressure", "temperature", "level"],
        "motor": ["motor", "drive", "vfd"],
        "exchanger": ["heat", "exchanger", "cooling"],
    }
    
    for eq_type, keywords in equipment_patterns.items():
        if any(keyword in filename_lower or keyword in content_lower[:1000] for keyword in keywords):
            equipment_type = eq_type.replace("_", " ").title()
            break
    
    # Make Detection (common industrial manufacturers)
    make_patterns = {
        "Flygt": ["flygt"],
        "ATC": ["atc"],
        "Siemens": ["siemens"],
        "ABB": ["abb"],
        "Schneider": ["schneider"],
        "Caterpillar": ["cat", "caterpillar"],
        "Grundfos": ["grundfos"],
        "Endress": ["endress", "hauser"],
        "Yokogawa": ["yokogawa"],
        "Emerson": ["emerson"],
        "Honeywell": ["honeywell"],
        "Generic": ["generic", "standard"]
    }
    
    for manufacturer, keywords in make_patterns.items():
        if any(keyword in filename_lower or keyword in content_lower[:1000] for keyword in keywords):
            make = manufacturer
            break
    
    # Model Detection (extract model numbers from filename)
    model_patterns = [
        r'(\d{4}[a-z]*)',  # 4 digits + optional letters (e.g., 3126, 600A)
        r'([a-z]+_?\d{3,4}[a-z]*)',  # letters + 3-4 digits (e.g., atc_600)
        r'(\d{1,2}[a-z]\d{2,3})',  # digit + letter + digits (e.g., 3A126)
    ]
    
    for pattern in model_patterns:
        matches = re.findall(pattern, filename_lower)
        if matches:
            model = matches[0].upper()
            break
    
    # Special handling for specific files
    if "flygt" in filename_lower:
        # Extract Flygt model numbers
        flygt_models = re.findall(r'(\d{4})', filename_lower)
        if flygt_models:
            model = f"Series {flygt_models[0]}"
        equipment_type = "Submersible Pump"
        make = "Flygt"
    
    elif "atc" in filename_lower and "flow" in filename_lower:
        model_match = re.search(r'(\d{3,4})', filename_lower)
        if model_match:
            model = f"ATC-{model_match.group(1)}"
        equipment_type = "Flow Meter"
        make = "ATC"
    
    elif "automatic_control" in filename_lower:
        model_match = re.search(r'(\d{4})', filename_lower)
        if model_match:
            model = f"AC-{model_match.group(1)}"
        equipment_type = "Control System"
        make = "Generic"
    
    return {
        "equipment_type": equipment_type,
        "make": make,
        "model": model,
        "filename": filename
    }

# =================================
# 🔧 Configuration Section - Using centralized config.py
# =================================
class VectorStoreConfig:
    """Configuration for vector store selection and parameters - uses config.py values."""
    
    # Vector store selection from config.py
    VECTOR_STORE: Literal['chromadb', 'faiss'] = VECTOR_STORE_TYPE  # From config.py
    
    # 🖼️ Image Processing Configuration
    ENABLE_IMAGE_PROCESSING: bool = False  # Set to True to enable image extraction and descriptions
    ENABLE_IMAGE_DESCRIPTIONS: bool = False  # Set to True for AI-generated image descriptions
    GENERATE_PAGE_IMAGES: bool = False  # Set to True to save full page images
    GENERATE_PICTURE_IMAGES: bool = False  # Set to True to save individual image crops
    IMAGE_SCALE: int = 2  # Image quality scale (1-3, higher = better quality but slower)
    
    # FAISS specific settings from config.py
    FAISS_INDEX_TYPE: Literal['flat', 'ivf', 'hnsw'] = FAISS_INDEX_TYPE  # From config.py
    FAISS_NLIST: int = 100  # Number of clusters for IVF
    FAISS_M: int = 16  # Number of connections for HNSW
    FAISS_EF_CONSTRUCTION: int = 200  # Construction parameter for HNSW
    
    # ChromaDB specific settings
    CHROMA_COLLECTION_NAME: str = "enhanced_pdf_chunks_v3"
    
    # Common settings from config.py
    EMBEDDING_MODEL_NAME: str = EMBEDDING_MODEL  # From config.py
    EMBEDDING_DIMENSION: int = EMBEDDING_DIMENSION  # From config.py
    BATCH_SIZE: int = EMBEDDING_BATCH_SIZE  # From config.py
    
    # Storage paths from config.py
    FAISS_INDEX_PATH: str = FAISS_INDEX_PATH  # From config.py
    FAISS_METADATA_PATH: str = FAISS_METADATA_PATH  # From config.py
    FAISS_JSON_PATH: str = FAISS_JSON_PATH  # From config.py

config = VectorStoreConfig()

# -----------------------------
# Helpers
# -----------------------------
def ensure_dirs():
    """Make sure all output directories exist before running pipeline."""
    for d in [MARKDOWN_DIR, CHUNKS_DIR, CHROMA_DB_DIR]:
        Path(d).mkdir(parents=True, exist_ok=True)
    
    # Ensure FAISS directory exists
    Path(config.FAISS_INDEX_PATH).parent.mkdir(parents=True, exist_ok=True)
    
    print(f"✅ Ensured directories: {MARKDOWN_DIR}, {CHUNKS_DIR}, {CHROMA_DB_DIR}")

def validate_dependencies():
    """Validate required dependencies based on configuration."""
    if config.VECTOR_STORE == 'faiss' and not FAISS_AVAILABLE:
        print("❌ FAISS selected but not available. Please install:")
        print("   pip install faiss-cpu  # for CPU version")
        print("   pip install faiss-gpu  # for GPU version")
        return False
    
    if not api_key:
        print("❌ OPENAI_API_KEY not found in environment variables!")
        return False
    
    return True


# -----------------------------
# 1️⃣ PDF Parsing with Docling
# -----------------------------
def convert_with_image_annotation(input_doc_path):
    """Convert PDF with configurable image processing settings."""
    # Build configurable pipeline options based on VectorStoreConfig settings
    pipeline_options = PdfPipelineOptions(
        do_ocr=False,                # keep embedded text layer only
        do_table_structure=True,     # still parse tables
        do_picture_description=VectorStoreConfig.ENABLE_IMAGE_DESCRIPTIONS,  # ✅ Configurable image captioning
        generate_page_images=VectorStoreConfig.GENERATE_PAGE_IMAGES,          # ✅ Configurable page images
        enable_remote_services=False,# no external API calls
        generate_picture_images=VectorStoreConfig.GENERATE_PICTURE_IMAGES,    # ✅ Configurable individual image crops
        images_scale=VectorStoreConfig.IMAGE_SCALE,                           # ✅ Configurable image quality
    )
    converter = DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
    )
    conv_res = converter.convert(source=input_doc_path)
    return conv_res

def export_single_md_with_images_and_serials(conv_res, output_path: Path):
    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)
    doc_filename = conv_res.input.file.stem.replace(" ", "_")
    md_filename = output_path / f"{doc_filename}-full-with-serials.md"

    conv_res.document.save_as_markdown(
        md_filename,
        image_mode=ImageRefMode.REFERENCED,
        include_annotations=True,
        page_break_placeholder="<!-- PAGE_BREAK -->",
    )

    # Add page-end markers
    with open(md_filename, "r", encoding="utf-8") as f:
        md_text = f.read()

    pages = md_text.split("<!-- PAGE_BREAK -->")
    final_md = ""
    for idx, page_text in enumerate(pages, start=1):
        page_text = page_text.strip()
        if not page_text:
            continue
        final_md += page_text + f"\n\n<!-- PAGE {idx} END -->\n\n"

    Path(md_filename).write_text(final_md, encoding="utf-8")
    print(f"✅ Markdown saved with serials → {md_filename}")
    return md_filename

def parse_pdfs():
    print("📄 Parsing PDFs with Docling pipeline...")
    markdown_files = []
    pdf_dir = Path(PDF_FOLDER)  # ✅ convert str → Path
    for pdf_path in pdf_dir.glob("*.pdf"):
        print(f"   ➡ Converting {pdf_path}")
        conv_res = convert_with_image_annotation(pdf_path)
        md_file = export_single_md_with_images_and_serials(conv_res, MARKDOWN_DIR)
        markdown_files.append(md_file)
    return markdown_files

# -----------------------------
# 2️⃣ Advanced Semantic Chunking
# -----------------------------
def smart_chunk_markdowns(markdown_files: List[str], max_tokens: int = MAX_TOKENS_PER_CHUNK, overlap_tokens: int = CHUNK_OVERLAP, model_name: str = "gpt-4o-mini") -> List[Dict[str, Any]]:
    """
    Advanced chunking with proper token counting, semantic boundaries, and overlap for better retrieval.
    """
    # Initialize tokenizer
    try:
        enc = tiktoken.encoding_for_model(model_name)
    except KeyError:
        enc = tiktoken.get_encoding("cl100k_base")  # fallback
    
    def count_tokens(text: str) -> int:
        return len(enc.encode(text))
    
    def clean_text(text: str) -> str:
        """Clean and normalize text while preserving structure."""
        # Remove excessive whitespace but preserve paragraph breaks
        text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
        # Clean up spaces
        text = re.sub(r'[ \t]+', ' ', text)
        return text.strip()
    
    def build_page_position_map(full_text: str) -> Dict[int, Dict[str, int]]:
        """
        🔧 FIXED: Build a map of page boundaries in the full document.
        Returns: {page_num: {'start_pos': int, 'end_pos': int}}
        """
        page_map = {}
        
        # Find all page end markers and their positions
        page_pattern = re.compile(r'<!-- PAGE (\d+) END -->')
        matches = list(page_pattern.finditer(full_text))
        
        if not matches:
            # No page markers found, treat as single page
            return {1: {'start_pos': 0, 'end_pos': len(full_text)}}
        
        # Build page boundaries
        for i, match in enumerate(matches):
            page_num = int(match.group(1))
            
            # Start position: end of previous page marker (or beginning of document)
            if i == 0:
                start_pos = 0
            else:
                start_pos = matches[i-1].end()
            
            # End position: start of current page marker
            end_pos = match.start()
            
            page_map[page_num] = {
                'start_pos': start_pos,
                'end_pos': end_pos
            }
        
        # Handle content after the last page marker
        last_match = matches[-1]
        last_page_num = int(last_match.group(1))
        if last_match.end() < len(full_text):
            # There's content after the last page marker - it belongs to next page
            next_page_num = last_page_num + 1
            page_map[next_page_num] = {
                'start_pos': last_match.end(),
                'end_pos': len(full_text)
            }
        
        return page_map
    
    def determine_chunk_pages(chunk_start: int, chunk_end: int, page_map: Dict[int, Dict[str, int]]) -> List[int]:
        """
        🔧 FIXED: Determine which page(s) a chunk belongs to based on its position.
        """
        chunk_pages = []
        
        for page_num, boundaries in page_map.items():
            page_start = boundaries['start_pos']
            page_end = boundaries['end_pos']
            
            # Check if chunk overlaps with this page
            if not (chunk_end <= page_start or chunk_start >= page_end):
                # There's overlap
                chunk_pages.append(page_num)
        
        # If no pages found (shouldn't happen), default to page 1
        return chunk_pages if chunk_pages else [1]
    
    def extract_context_info(text: str, chunk_start: int = 0, chunk_end: int = None, page_map: Dict[int, Dict[str, int]] = None) -> Dict[str, Any]:
        """
        🔧 FIXED: Extract metadata with correct page attribution.
        """
        heading_pattern = re.compile(r'^(#+)\s+(.+)$', re.MULTILINE)
        table_pattern = re.compile(r'\|.*\|', re.MULTILINE)
        figure_pattern = re.compile(r'!\[.*?\]\(.*?\)', re.MULTILINE)
        
        # Use position-based page detection if page_map provided, otherwise fallback to old method
        if page_map is not None and chunk_end is not None:
            pages = determine_chunk_pages(chunk_start, chunk_end, page_map)
        else:
            # Fallback to old method for backward compatibility
            page_pattern = re.compile(r'<!-- PAGE (\d+) END -->')
            pages = [int(p) for p in page_pattern.findall(text)]
            if not pages:
                pages = [1]
        
        headings = [(len(h[0]), h[1]) for h in heading_pattern.findall(text)]
        has_tables = len(table_pattern.findall(text)) > 0
        has_figures = len(figure_pattern.findall(text)) > 0
        
        return {
            'pages': sorted(set(pages)),  # 🔧 FIXED: Now correctly determined by position
            'headings': headings,
            'has_tables': has_tables,
            'has_figures': has_figures,
            'main_heading': headings[0][1] if headings else ""
        }
    
    def split_by_sentences(text: str, max_tokens: int) -> List[str]:
        """Split text by sentences when a chunk is too large."""
        sentences = re.split(r'(?<=[.!?])\s+', text)
        chunks = []
        current = []
        current_tokens = 0
        
        for sentence in sentences:
            sentence_tokens = count_tokens(sentence)
            if current_tokens + sentence_tokens > max_tokens and current:
                chunks.append(' '.join(current))
                current = [sentence]
                current_tokens = sentence_tokens
            else:
                current.append(sentence)
                current_tokens += sentence_tokens
        
        if current:
            chunks.append(' '.join(current))
        
        return chunks
    
    all_chunks = []
    
    for md_file in markdown_files:
        print(f"🔍 Processing {Path(md_file).name} with advanced chunking...")
        
        md_file = Path(md_file)
        with md_file.open("r", encoding="utf-8") as f:
            md_text = f.read()
        
        # 🏭 Extract equipment metadata from filename and content
        equipment_metadata = extract_equipment_metadata(md_file.name, md_text)
        print(f"   🏭 Equipment detected: {equipment_metadata['make']} {equipment_metadata['model']} ({equipment_metadata['equipment_type']})")
        
        # Clean the text
        cleaned_text = clean_text(md_text)
        
        # 🔧 FIXED: Build page position map for accurate page attribution
        page_map = build_page_position_map(md_text)
        print(f"   📄 Page boundaries detected: {list(page_map.keys())}")
        
        # Split by major sections (headers)
        sections = re.split(r'(?=^#+\s)', cleaned_text, flags=re.MULTILINE)
        sections = [s.strip() for s in sections if s.strip()]
        
        file_chunks = []
        
        for section in sections:
            section_tokens = count_tokens(section)
            
            # Find this section's position in the original text
            section_start = md_text.find(section)
            if section_start == -1:
                # Fallback: try to find a substring
                section_preview = section[:100]
                section_start = md_text.find(section_preview)
            
            if section_tokens <= max_tokens:
                # Section fits in one chunk
                section_end = section_start + len(section) if section_start != -1 else len(section)
                context = extract_context_info(section, section_start, section_end, page_map)
                file_chunks.append({
                    'chunk_text': section,
                    'token_count': section_tokens,
                    **context
                })
            else:
                # 🔧 FIXED: Section is too large, split by sentences with proper page tracking
                sentences = re.split(r'(?<=[.!?])\s+', section)
                current_chunk = []
                current_tokens = 0
                current_start = section_start
                
                for sentence in sentences:
                    sentence_tokens = count_tokens(sentence)
                    
                    if current_tokens + sentence_tokens > max_tokens and current_chunk:
                        # Save current chunk
                        chunk_text = ' '.join(current_chunk)
                        chunk_end = current_start + len(chunk_text) if current_start != -1 else len(chunk_text)
                        context = extract_context_info(chunk_text, current_start, chunk_end, page_map)
                        
                        file_chunks.append({
                            'chunk_text': chunk_text,
                            'token_count': count_tokens(chunk_text),
                            **context
                        })
                        
                        # Start new chunk
                        current_chunk = [sentence]
                        current_tokens = sentence_tokens
                        current_start = chunk_end  # Update start position
                    else:
                        current_chunk.append(sentence)
                        current_tokens += sentence_tokens
                
                # Save remaining chunk
                if current_chunk:
                    chunk_text = ' '.join(current_chunk)
                    chunk_end = current_start + len(chunk_text) if current_start != -1 else len(chunk_text)
                    context = extract_context_info(chunk_text, current_start, chunk_end, page_map)
                    
                    file_chunks.append({
                        'chunk_text': chunk_text,
                        'token_count': count_tokens(chunk_text),
                        **context
                    })
        
        # Add overlap between chunks for better continuity
        overlapped_chunks = []
        for i, chunk in enumerate(file_chunks):
            # Create overlapped version
            overlap_text = ""
            
            # Add previous context if exists
            if i > 0 and overlap_tokens > 0:
                prev_text = file_chunks[i-1]['chunk_text']
                prev_sentences = re.split(r'(?<=[.!?])\s+', prev_text)
                
                # Take last few sentences from previous chunk
                overlap_part = []
                overlap_token_count = 0
                for sentence in reversed(prev_sentences):
                    sentence_tokens = count_tokens(sentence)
                    if overlap_token_count + sentence_tokens <= overlap_tokens:
                        overlap_part.insert(0, sentence)
                        overlap_token_count += sentence_tokens
                    else:
                        break
                
                if overlap_part:
                    overlap_text = "...[Previous context: " + " ".join(overlap_part) + "]\n\n"
            
            final_chunk_text = overlap_text + chunk['chunk_text']
            
            overlapped_chunks.append({
                'chunk_text': final_chunk_text,
                'original_text': chunk['chunk_text'],  # Keep original for metadata
                'token_count': count_tokens(final_chunk_text),
                'pages': chunk['pages'],
                'heading': chunk['main_heading'],
                'has_tables': chunk.get('has_tables', False),
                'has_figures': chunk.get('has_figures', False),
                'chunk_index': i,
                'source_file': md_file.stem,
                # 🏭 Equipment metadata for filtering
                'equipment_type': equipment_metadata['equipment_type'],
                'make': equipment_metadata['make'],
                'model': equipment_metadata['model'],
                'equipment_filename': equipment_metadata['filename']
            })
        
        # Save enhanced chunks JSON
        json_path = Path(CHUNKS_DIR) / f"{md_file.stem}_smart_chunks.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(overlapped_chunks, f, ensure_ascii=False, indent=2)
        
        print(f"✅ {len(overlapped_chunks)} smart chunks saved → {json_path}")
        print(f"   📊 Avg tokens per chunk: {sum(c['token_count'] for c in overlapped_chunks) // len(overlapped_chunks)}")
        
        # 🔧 FIXED: Show page distribution for debugging
        page_distribution = {}
        for chunk in overlapped_chunks:
            for page in chunk['pages']:
                page_distribution[page] = page_distribution.get(page, 0) + 1
        print(f"   📄 Page distribution: {dict(sorted(page_distribution.items()))}")
        
        all_chunks.extend(overlapped_chunks)
    
    return all_chunks

# Backward compatibility wrapper
def chunk_markdowns(markdown_files, max_tokens=MAX_TOKENS_PER_CHUNK):
    """Wrapper for backward compatibility."""
    return smart_chunk_markdowns(markdown_files, max_tokens)

# -----------------------------
# 3️⃣ Vector Store Implementations
# -----------------------------

class BaseVectorStore:
    """Base class for vector stores."""
    
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            api_key=api_key,
            model=config.EMBEDDING_MODEL_NAME
        )
    
    def add_documents(self, chunks: List[Dict[str, Any]]) -> bool:
        """Add documents to the vector store."""
        raise NotImplementedError
    
    def query(self, query: str, n_results: int = 5) -> Dict[str, Any]:
        """Query the vector store."""
        raise NotImplementedError
    
    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about the vector store."""
        raise NotImplementedError

class ChromaDBVectorStore(BaseVectorStore):
    """ChromaDB implementation."""
    
    def __init__(self):
        super().__init__()
        self.client = chromadb.PersistentClient(path=str(CHROMA_DB_DIR))
        self.collection = None
    
    def add_documents(self, chunks: List[Dict[str, Any]]) -> bool:
        """Add documents to ChromaDB."""
        print("🔎 Building ChromaDB embeddings with rich metadata...")
        
        if not chunks:
            print("⚠️ No chunks provided.")
            return False
        
        # Delete existing collection if exists
        existing = [c.name for c in self.client.list_collections()]
        if config.CHROMA_COLLECTION_NAME in existing:
            self.client.delete_collection(config.CHROMA_COLLECTION_NAME)
            print(f"🗑 Deleted existing collection '{config.CHROMA_COLLECTION_NAME}'")
        
        # Create new collection
        self.collection = self.client.create_collection(
            name=config.CHROMA_COLLECTION_NAME,
            embedding_function=embedding_functions.OpenAIEmbeddingFunction(
                api_key=api_key,
                model_name=config.EMBEDDING_MODEL_NAME
            )
        )
        
        # Prepare data
        ids, texts, metadatas = self._prepare_data(chunks)
        
        # Add documents in batches
        total_added = 0
        for i in range(0, len(texts), config.BATCH_SIZE):
            batch_ids = ids[i:i+config.BATCH_SIZE]
            batch_texts = texts[i:i+config.BATCH_SIZE]
            batch_metadatas = metadatas[i:i+config.BATCH_SIZE]
            
            try:
                self.collection.add(
                    ids=batch_ids,
                    documents=batch_texts,
                    metadatas=batch_metadatas,
                )
                total_added += len(batch_ids)
                print(f"   📦 Added batch {i//config.BATCH_SIZE + 1}: {len(batch_ids)} chunks (Total: {total_added}/{len(texts)})")
                
            except Exception as e:
                print(f"❌ Error adding batch {i//config.BATCH_SIZE + 1}: {str(e)}")
                continue
        
        print(f"✅ Stored {total_added} chunks in ChromaDB")
        return True
    
    def query(self, query: str, n_results: int = 5) -> Dict[str, Any]:
        """Query ChromaDB."""
        if not self.collection:
            return {"documents": [], "metadatas": [], "distances": []}
        
        try:
            results = self.collection.query(
                query_texts=[query],
                n_results=n_results,
                include=['documents', 'metadatas', 'distances']
            )
            return {
                "documents": results['documents'][0] if results['documents'] else [],
                "metadatas": results['metadatas'][0] if results['metadatas'] else [],
                "distances": results['distances'][0] if results['distances'] else []
            }
        except Exception as e:
            print(f"❌ ChromaDB query error: {str(e)}")
            return {"documents": [], "metadatas": [], "distances": []}
    
    def get_stats(self) -> Dict[str, Any]:
        """Get ChromaDB statistics."""
        if not self.collection:
            return {"total_documents": 0}
        
        try:
            count = len(self.collection.get()['ids'])
            return {"total_documents": count, "collection_name": config.CHROMA_COLLECTION_NAME}
        except:
            return {"total_documents": 0}
    
    def _prepare_data(self, chunks: List[Dict[str, Any]]):
        """Prepare data for ChromaDB."""
        ids, texts, metadatas = [], [], []
        
        for i, chunk in enumerate(chunks):
            chunk_id = f"{chunk.get('source_file', 'unknown')}_{chunk.get('chunk_index', i)}"
            ids.append(chunk_id)
            texts.append(chunk['chunk_text'])
            
            metadata = {
                'pages': ','.join(map(str, chunk.get('pages', [1]))),
                'page_count': len(chunk.get('pages', [1])),
                'heading': chunk.get('heading', ''),
                'source_file': chunk.get('source_file', ''),
                'chunk_index': chunk.get('chunk_index', i),
                'token_count': chunk.get('token_count', 0),
                'has_tables': chunk.get('has_tables', False),
                'has_figures': chunk.get('has_figures', False),
                'content_type': 'mixed' if (chunk.get('has_tables', False) or chunk.get('has_figures', False)) else 'text',
                'text_length': len(chunk.get('original_text', chunk['chunk_text'])),
                'is_introduction': bool(re.search(r'\b(introduction|overview|summary)\b', chunk.get('heading', ''), re.IGNORECASE)),
                'is_conclusion': bool(re.search(r'\b(conclusion|summary|results?|findings?)\b', chunk.get('heading', ''), re.IGNORECASE)),
                'is_technical': bool(re.search(r'\b(algorithm|method|approach|implementation|technical|specification)\b', chunk['chunk_text'], re.IGNORECASE)),
                # 🏭 Equipment metadata for filtering
                'equipment_type': chunk.get('equipment_type', 'Unknown'),
                'make': chunk.get('make', 'Unknown'),
                'model': chunk.get('model', 'Unknown'),
                'equipment_filename': chunk.get('equipment_filename', ''),
            }
            
            # Convert values to strings for Chroma compatibility
            for key, value in metadata.items():
                if isinstance(value, bool):
                    metadata[key] = str(value)
                elif isinstance(value, (int, float)):
                    metadata[key] = str(value)
            
            metadatas.append(metadata)
        
        return ids, texts, metadatas

class FAISSVectorStore(BaseVectorStore):
    """FAISS implementation with metadata support."""
    
    def __init__(self):
        super().__init__()
        self.index = None
        self.metadata_store = []
        self.id_to_index = {}
    
    def add_documents(self, chunks: List[Dict[str, Any]]) -> bool:
        """Add documents to FAISS."""
        print(f"🔎 Building FAISS embeddings ({config.FAISS_INDEX_TYPE}) with metadata...")
        
        if not chunks:
            print("⚠️ No chunks provided.")
            return False
        
        # Prepare texts for embedding
        texts = [chunk['chunk_text'] for chunk in chunks]
        print(f"   🔄 Generating embeddings for {len(texts)} chunks...")
        
        try:
            # Generate embeddings in batches
            all_embeddings = []
            for i in range(0, len(texts), config.BATCH_SIZE):
                batch_texts = texts[i:i+config.BATCH_SIZE]
                batch_embeddings = self.embeddings.embed_documents(batch_texts)
                all_embeddings.extend(batch_embeddings)
                print(f"   📦 Generated embeddings for batch {i//config.BATCH_SIZE + 1}: {len(batch_texts)} chunks")
            
            # Convert to numpy array
            embeddings_array = np.array(all_embeddings, dtype=np.float32)
            print(f"   📊 Embeddings shape: {embeddings_array.shape}")
            
            # Create FAISS index based on configuration
            dimension = embeddings_array.shape[1]
            
            if config.FAISS_INDEX_TYPE == 'flat':
                self.index = faiss.IndexFlatIP(dimension)  # Inner product for cosine similarity
                
            elif config.FAISS_INDEX_TYPE == 'ivf':
                quantizer = faiss.IndexFlatIP(dimension)
                self.index = faiss.IndexIVFFlat(quantizer, dimension, config.FAISS_NLIST)
                # Train the index
                print(f"   🏋️ Training IVF index with {config.FAISS_NLIST} clusters...")
                self.index.train(embeddings_array)
                
            elif config.FAISS_INDEX_TYPE == 'hnsw':
                self.index = faiss.IndexHNSWFlat(dimension, config.FAISS_M)
                self.index.hnsw.efConstruction = config.FAISS_EF_CONSTRUCTION
                
            else:
                raise ValueError(f"Unsupported FAISS index type: {config.FAISS_INDEX_TYPE}")
            
            # Normalize embeddings for cosine similarity
            faiss.normalize_L2(embeddings_array)
            
            # Add embeddings to index
            self.index.add(embeddings_array)
            
            # Store metadata separately
            self.metadata_store = []
            self.id_to_index = {}
            
            for i, chunk in enumerate(chunks):
                chunk_id = f"{chunk.get('source_file', 'unknown')}_{chunk.get('chunk_index', i)}"
                self.id_to_index[chunk_id] = i
                
                metadata = {
                    'id': chunk_id,
                    'text': chunk['chunk_text'],
                    'original_text': chunk.get('original_text', chunk['chunk_text']),
                    'pages': chunk.get('pages', [1]),
                    'page_count': len(chunk.get('pages', [1])),
                    'heading': chunk.get('heading', ''),
                    'source_file': chunk.get('source_file', ''),
                    'chunk_index': chunk.get('chunk_index', i),
                    'token_count': chunk.get('token_count', 0),
                    'has_tables': chunk.get('has_tables', False),
                    'has_figures': chunk.get('has_figures', False),
                    'content_type': 'mixed' if (chunk.get('has_tables', False) or chunk.get('has_figures', False)) else 'text',
                    'text_length': len(chunk.get('original_text', chunk['chunk_text'])),
                    'is_introduction': bool(re.search(r'\b(introduction|overview|summary)\b', chunk.get('heading', ''), re.IGNORECASE)),
                    'is_conclusion': bool(re.search(r'\b(conclusion|summary|results?|findings?)\b', chunk.get('heading', ''), re.IGNORECASE)),
                    'is_technical': bool(re.search(r'\b(algorithm|method|approach|implementation|technical|specification)\b', chunk['chunk_text'], re.IGNORECASE)),
                    # 🏭 Equipment metadata for filtering
                    'equipment_type': chunk.get('equipment_type', 'Unknown'),
                    'make': chunk.get('make', 'Unknown'),
                    'model': chunk.get('model', 'Unknown'),
                    'equipment_filename': chunk.get('equipment_filename', ''),
                }
                self.metadata_store.append(metadata)
            
            # Save index and metadata to disk
            self._save_to_disk()
            
            print(f"✅ Stored {len(chunks)} chunks in FAISS ({config.FAISS_INDEX_TYPE}) index")
            return True
            
        except Exception as e:
            print(f"❌ Error building FAISS index: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    
    def query(self, query: str, n_results: int = 5) -> Dict[str, Any]:
        """Query FAISS index."""
        if self.index is None:
            # Try to load from disk
            if not self._load_from_disk():
                return {"documents": [], "metadatas": [], "distances": []}
        
        try:
            # Generate query embedding
            query_embedding = self.embeddings.embed_query(query)
            query_vector = np.array([query_embedding], dtype=np.float32)
            faiss.normalize_L2(query_vector)
            
            # Search
            scores, indices = self.index.search(query_vector, n_results)
            
            # Prepare results
            documents = []
            metadatas = []
            distances = []
            
            for score, idx in zip(scores[0], indices[0]):
                if idx >= 0 and idx < len(self.metadata_store):
                    metadata = self.metadata_store[idx]
                    documents.append(metadata['text'])
                    
                    # Convert metadata for compatibility with ChromaDB format
                    meta_dict = {
                        'pages': ','.join(map(str, metadata['pages'])),
                        'page_count': str(metadata['page_count']),
                        'heading': metadata['heading'],
                        'source_file': metadata['source_file'],
                        'chunk_index': str(metadata['chunk_index']),
                        'token_count': str(metadata['token_count']),
                        'has_tables': str(metadata['has_tables']),
                        'has_figures': str(metadata['has_figures']),
                        'content_type': metadata['content_type'],
                        'text_length': str(metadata['text_length']),
                        'is_introduction': str(metadata['is_introduction']),
                        'is_conclusion': str(metadata['is_conclusion']),
                        'is_technical': str(metadata['is_technical']),
                        # 🏭 Equipment metadata for filtering
                        'equipment_type': metadata.get('equipment_type', 'Unknown'),
                        'make': metadata.get('make', 'Unknown'),
                        'model': metadata.get('model', 'Unknown'),
                        'equipment_filename': metadata.get('equipment_filename', ''),
                    }
                    metadatas.append(meta_dict)
                    distances.append(1.0 - score)  # Convert similarity to distance
            
            return {
                "documents": documents,
                "metadatas": metadatas,
                "distances": distances
            }
            
        except Exception as e:
            print(f"❌ FAISS query error: {str(e)}")
            return {"documents": [], "metadatas": [], "distances": []}
    
    def query_with_equipment_filter(self, query: str, equipment_filter: Dict[str, str] = None, n_results: int = 5) -> Dict[str, Any]:
        """
        Query FAISS index with equipment-based metadata filtering.
        
        Args:
            query: The search query
            equipment_filter: Dict with keys 'make', 'model', 'equipment_type' for filtering
            n_results: Number of results to return
        
        Returns:
            Filtered results based on equipment metadata
        """
        if self.index is None:
            if not self._load_from_disk():
                return {"documents": [], "metadatas": [], "distances": []}
        
        try:
            # First get more results than needed to allow for filtering
            search_limit = min(n_results * 3, len(self.metadata_store))  # Get 3x more for filtering
            
            # Generate query embedding
            query_embedding = self.embeddings.embed_query(query)
            query_vector = np.array([query_embedding], dtype=np.float32)
            faiss.normalize_L2(query_vector)
            
            # Search with larger limit
            scores, indices = self.index.search(query_vector, search_limit)
            
            # Apply equipment filtering
            filtered_results = []
            
            for score, idx in zip(scores[0], indices[0]):
                if idx >= 0 and idx < len(self.metadata_store):
                    metadata = self.metadata_store[idx]
                    
                    # Apply equipment filter if provided
                    if equipment_filter:
                        match = True
                        for filter_key, filter_value in equipment_filter.items():
                            if filter_value and filter_value.lower() != 'unknown':
                                metadata_value = metadata.get(filter_key, '').lower()
                                if filter_value.lower() not in metadata_value:
                                    match = False
                                    break
                        if not match:
                            continue
                    
                    filtered_results.append((score, idx, metadata))
                    
                    # Stop when we have enough results
                    if len(filtered_results) >= n_results:
                        break
            
            # Prepare final results
            documents = []
            metadatas = []
            distances = []
            
            for score, idx, metadata in filtered_results:
                documents.append(metadata['text'])
                
                # Convert metadata for compatibility
                meta_dict = {
                    'pages': ','.join(map(str, metadata['pages'])),
                    'page_count': str(metadata['page_count']),
                    'heading': metadata['heading'],
                    'source_file': metadata['source_file'],
                    'chunk_index': str(metadata['chunk_index']),
                    'token_count': str(metadata['token_count']),
                    'has_tables': str(metadata['has_tables']),
                    'has_figures': str(metadata['has_figures']),
                    'content_type': metadata['content_type'],
                    'text_length': str(metadata['text_length']),
                    'is_introduction': str(metadata['is_introduction']),
                    'is_conclusion': str(metadata['is_conclusion']),
                    'is_technical': str(metadata['is_technical']),
                    'equipment_type': metadata.get('equipment_type', 'Unknown'),
                    'make': metadata.get('make', 'Unknown'),
                    'model': metadata.get('model', 'Unknown'),
                    'equipment_filename': metadata.get('equipment_filename', ''),
                }
                metadatas.append(meta_dict)
                distances.append(1.0 - score)  # Convert similarity to distance
            
            print(f"🏭 Equipment Filter Applied: {equipment_filter}")
            print(f"📋 Found {len(filtered_results)} filtered results from {len(self.metadata_store)} total chunks")
            
            return {
                "documents": documents,
                "metadatas": metadatas,
                "distances": distances
            }
            
        except Exception as e:
            print(f"❌ FAISS equipment query error: {str(e)}")
            return {"documents": [], "metadatas": [], "distances": []}
    
    def get_stats(self) -> Dict[str, Any]:
        """Get FAISS statistics."""
        if self.index is None:
            self._load_from_disk()
        
        if self.index is None:
            return {"total_documents": 0}
        
        return {
            "total_documents": self.index.ntotal,
            "index_type": config.FAISS_INDEX_TYPE,
            "dimension": self.index.d if hasattr(self.index, 'd') else config.EMBEDDING_DIMENSION
        }
    
    def _save_to_disk(self):
        """Save FAISS index and metadata to disk."""
        try:
            # Save FAISS index (binary)
            faiss.write_index(self.index, config.FAISS_INDEX_PATH)
            
            # Save metadata (pickle for fast loading)
            with open(config.FAISS_METADATA_PATH, 'wb') as f:
                pickle.dump({
                    'metadata_store': self.metadata_store,
                    'id_to_index': self.id_to_index
                }, f)
            
            # 🆕 Save human-readable metadata JSON
            with open(config.FAISS_JSON_PATH, 'w', encoding='utf-8') as f:
                json.dump({
                    'config': {
                        'index_type': config.FAISS_INDEX_TYPE,
                        'total_documents': len(self.metadata_store),
                        'embedding_model': config.EMBEDDING_MODEL_NAME,
                        'embedding_dimension': config.EMBEDDING_DIMENSION,
                        'batch_size': config.BATCH_SIZE,
                        'created_at': datetime.now().isoformat()
                    },
                    'statistics': {
                        'total_chunks': len(self.metadata_store),
                        'chunks_with_tables': sum(1 for m in self.metadata_store if m.get('has_tables', False)),
                        'chunks_with_figures': sum(1 for m in self.metadata_store if m.get('has_figures', False)),
                        'technical_chunks': sum(1 for m in self.metadata_store if m.get('is_technical', False)),
                        'avg_token_count': sum(m.get('token_count', 0) for m in self.metadata_store) / len(self.metadata_store) if self.metadata_store else 0,
                        'source_files': list(set(m.get('source_file', 'unknown') for m in self.metadata_store)),
                        'page_range': {
                            'min_page': min(min(m.get('pages', [1])) for m in self.metadata_store) if self.metadata_store else 1,
                            'max_page': max(max(m.get('pages', [1])) for m in self.metadata_store) if self.metadata_store else 1
                        }
                    },
                    'documents': self.metadata_store
                }, f, ensure_ascii=False, indent=2, default=str)
            
            print(f"💾 FAISS index saved to: {config.FAISS_INDEX_PATH}")
            print(f"💾 Metadata (pickle) saved to: {config.FAISS_METADATA_PATH}")
            print(f"📄 Human-readable metadata saved to: {config.FAISS_JSON_PATH}")
            
        except Exception as e:
            print(f"❌ Error saving FAISS to disk: {str(e)}")
    
    def _load_from_disk(self) -> bool:
        """Load FAISS index and metadata from disk."""
        try:
            # Check if files exist
            if not Path(config.FAISS_INDEX_PATH).exists() or not Path(config.FAISS_METADATA_PATH).exists():
                return False
            
            # Load FAISS index
            self.index = faiss.read_index(config.FAISS_INDEX_PATH)
            
            # Load metadata
            with open(config.FAISS_METADATA_PATH, 'rb') as f:
                data = pickle.load(f)
                self.metadata_store = data['metadata_store']
                self.id_to_index = data['id_to_index']
            
            print(f"📂 FAISS index loaded from: {config.FAISS_INDEX_PATH}")
            print(f"📂 Metadata loaded from: {config.FAISS_METADATA_PATH}")
            if Path(config.FAISS_JSON_PATH).exists():
                print(f"📄 Human-readable metadata available at: {config.FAISS_JSON_PATH}")
            return True
            
        except Exception as e:
            print(f"❌ Error loading FAISS from disk: {str(e)}")
            return False

# -----------------------------
# 4️⃣ Vector Store Factory
# -----------------------------

def create_vector_store() -> BaseVectorStore:
    """Factory function to create the appropriate vector store."""
    if config.VECTOR_STORE == 'chromadb':
        print(f"🏗️ Using ChromaDB vector store")
        return ChromaDBVectorStore()
    elif config.VECTOR_STORE == 'faiss':
        if not FAISS_AVAILABLE:
            print("❌ FAISS not available, falling back to ChromaDB")
            config.VECTOR_STORE = 'chromadb'
            return ChromaDBVectorStore()
        print(f"🏗️ Using FAISS vector store ({config.FAISS_INDEX_TYPE})")
        return FAISSVectorStore()
    else:
        raise ValueError(f"Unsupported vector store: {config.VECTOR_STORE}")

def get_available_equipment() -> Dict[str, List[str]]:
    """Get all available equipment types, makes, and models from the vector store."""
    if not Path(config.FAISS_JSON_PATH).exists():
        print(f"❌ FAISS JSON metadata not found at: {config.FAISS_JSON_PATH}")
        return {}
    
    try:
        with open(config.FAISS_JSON_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        equipment_types = set()
        makes = set()
        models = set()
        
        for doc in data.get('documents', []):
            equipment_types.add(doc.get('equipment_type', 'Unknown'))
            makes.add(doc.get('make', 'Unknown'))
            models.add(doc.get('model', 'Unknown'))
        
        result = {
            'equipment_types': sorted(list(equipment_types)),
            'makes': sorted(list(makes)),
            'models': sorted(list(models))
        }
        
        print(f"🏭 Available Equipment:")
        print(f"   • Equipment Types: {', '.join(result['equipment_types'])}")
        print(f"   • Makes: {', '.join(result['makes'])}")  
        print(f"   • Models: {', '.join(result['models'])}")
        
        return result
        
    except Exception as e:
        print(f"❌ Error reading equipment data: {str(e)}")
        return {}

def inspect_faiss_metadata() -> Dict[str, Any]:
    """Inspect stored FAISS metadata without loading the full index."""
    if not Path(config.FAISS_JSON_PATH).exists():
        print(f"❌ FAISS JSON metadata not found at: {config.FAISS_JSON_PATH}")
        return {}
    
    try:
        with open(config.FAISS_JSON_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"📊 FAISS Metadata Summary:")
        print(f"   • Index Type: {data['config']['index_type']}")
        print(f"   • Total Documents: {data['config']['total_documents']}")
        print(f"   • Embedding Model: {data['config']['embedding_model']}")
        print(f"   • Created: {data['config']['created_at']}")
        print(f"   • Chunks with Tables: {data['statistics']['chunks_with_tables']}")
        print(f"   • Chunks with Figures: {data['statistics']['chunks_with_figures']}")
        print(f"   • Technical Chunks: {data['statistics']['technical_chunks']}")
        print(f"   • Average Tokens: {data['statistics']['avg_token_count']:.1f}")
        print(f"   • Source Files: {', '.join(data['statistics']['source_files'])}")
        print(f"   • Page Range: {data['statistics']['page_range']['min_page']}-{data['statistics']['page_range']['max_page']}")
        
        # 🏭 Equipment breakdown
        if 'documents' in data:
            equipment_stats = {}
            for doc in data['documents']:
                eq_key = f"{doc.get('make', 'Unknown')} {doc.get('model', 'Unknown')} ({doc.get('equipment_type', 'Unknown')})"
                equipment_stats[eq_key] = equipment_stats.get(eq_key, 0) + 1
            
            print(f"\n🏭 Equipment Breakdown:")
            for equipment, count in sorted(equipment_stats.items()):
                print(f"   • {equipment}: {count} chunks")
        
        return data
        
    except Exception as e:
        print(f"❌ Error reading FAISS metadata: {str(e)}")
        return {}

def list_vector_store_files():
    """List all vector store related files."""
    print(f"📁 Vector Store Files Summary:")
    print(f"=" * 50)
    
    # Check chunks directory
    chunks_dir = Path(CHUNKS_DIR)
    if chunks_dir.exists():
        chunk_files = list(chunks_dir.glob("*_smart_chunks.json"))
        print(f"📝 Chunk Files ({len(chunk_files)}):")
        for file in chunk_files:
            size_kb = file.stat().st_size / 1024
            print(f"   • {file.name} ({size_kb:.1f} KB)")
    
    # Check vector store files
    chroma_dir = Path(CHROMA_DB_DIR)
    if chroma_dir.exists():
        print(f"\n🗄️ Vector Store Files:")
        
        # FAISS files
        if Path(config.FAISS_INDEX_PATH).exists():
            size_mb = Path(config.FAISS_INDEX_PATH).stat().st_size / (1024 * 1024)
            print(f"   • faiss_index ({size_mb:.1f} MB) - Binary FAISS vectors")
        
        if Path(config.FAISS_METADATA_PATH).exists():
            size_kb = Path(config.FAISS_METADATA_PATH).stat().st_size / 1024
            print(f"   • faiss_metadata.pkl ({size_kb:.1f} KB) - Fast metadata")
        
        if Path(config.FAISS_JSON_PATH).exists():
            size_kb = Path(config.FAISS_JSON_PATH).stat().st_size / 1024
            print(f"   • faiss_metadata.json ({size_kb:.1f} KB) - Human-readable metadata")
        
        # ChromaDB files
        chroma_files = list(chroma_dir.rglob("*"))
        chroma_files = [f for f in chroma_files if f.is_file() and 'faiss' not in f.name]
        if chroma_files:
            total_size = sum(f.stat().st_size for f in chroma_files) / (1024 * 1024)
            print(f"   • ChromaDB files ({len(chroma_files)} files, {total_size:.1f} MB)")

def build_enhanced_embeddings(chunks: List[Dict[str, Any]]) -> BaseVectorStore:
    """Build embeddings using the configured vector store."""
    vector_store = create_vector_store()
    
    if vector_store.add_documents(chunks):
        # Print statistics
        stats = vector_store.get_stats()
        print(f"� Vector Store Statistics:")
        for key, value in stats.items():
            print(f"   • {key}: {value}")
        
        # Calculate chunk statistics
        if chunks:
            avg_tokens = sum(c.get('token_count', 0) for c in chunks) // len(chunks)
            tables_count = sum(1 for c in chunks if c.get('has_tables', False))
            figures_count = sum(1 for c in chunks if c.get('has_figures', False))
            technical_count = sum(1 for c in chunks if bool(re.search(r'\b(algorithm|method|approach|implementation|technical|specification)\b', c.get('chunk_text', ''), re.IGNORECASE)))
            
            print(f"� Chunk Statistics:")
            print(f"   • Average tokens per chunk: {avg_tokens}")
            print(f"   • Chunks with tables: {tables_count}")
            print(f"   • Chunks with figures: {figures_count}")
            print(f"   • Technical content chunks: {technical_count}")
        
        return vector_store
    else:
        return None

# Test retrieval function for new vector store system
def test_retrieval(vector_store: BaseVectorStore, query: str, n_results: int = 5):
    """Test the retrieval system with a query."""
    if not vector_store:
        print("❌ No vector store available for testing")
        return
    
    print(f"\n🔍 Testing retrieval with query: '{query}'")
    
    try:
        results = vector_store.query(query, n_results)
        
        if not results["documents"]:
            print("❌ No results found")
            return
        
        print(f"📋 Found {len(results['documents'])} results:")
        
        for i, (doc, metadata, distance) in enumerate(zip(
            results['documents'], 
            results['metadatas'], 
            results['distances']
        )):
            score = 1 - distance if distance <= 1 else distance
            print(f"\n{i+1}. [Score: {score:.3f}] {metadata.get('heading', 'No heading')}")
            print(f"   📄 Pages: {metadata.get('pages', 'Unknown')} | File: {metadata.get('source_file', 'Unknown')}")
            print(f"   🏷️  Type: {metadata.get('content_type', 'text')} | Tokens: {metadata.get('token_count', 'Unknown')}")
            print(f"   🏭 Equipment: {metadata.get('make', 'Unknown')} {metadata.get('model', 'Unknown')} ({metadata.get('equipment_type', 'Unknown')})")
            print(f"   📝 Preview: {doc[:200]}...")
            
    except Exception as e:
        print(f"❌ Error during retrieval test: {str(e)}")

def test_equipment_filtering(vector_store: BaseVectorStore, query: str, equipment_filter: Dict[str, str] = None, n_results: int = 3):
    """Test equipment-based filtering on FAISS vector store."""
    if not isinstance(vector_store, FAISSVectorStore):
        print("⚠️ Equipment filtering only available for FAISS vector store")
        return
    
    print(f"\n🏭 Testing equipment filtering with query: '{query}'")
    if equipment_filter:
        print(f"   🔍 Filter: {equipment_filter}")
    
    try:
        results = vector_store.query_with_equipment_filter(query, equipment_filter, n_results)
        
        if not results["documents"]:
            print("❌ No results found with the given filter")
            return
        
        print(f"📋 Found {len(results['documents'])} filtered results:")
        
        for i, (doc, metadata, distance) in enumerate(zip(
            results['documents'], 
            results['metadatas'], 
            results['distances']
        )):
            score = 1 - distance if distance <= 1 else distance
            print(f"\n{i+1}. [Score: {score:.3f}] {metadata.get('heading', 'No heading')}")
            print(f"   📄 Pages: {metadata.get('pages', 'Unknown')} | File: {metadata.get('source_file', 'Unknown')}")
            print(f"   🏭 Equipment: {metadata.get('make', 'Unknown')} {metadata.get('model', 'Unknown')} ({metadata.get('equipment_type', 'Unknown')})")
            print(f"   📝 Preview: {doc[:150]}...")
            
    except Exception as e:
        print(f"❌ Error during equipment filtering test: {str(e)}")

# Backward compatibility wrapper
def build_embeddings(chunks):
    """Wrapper for backward compatibility."""
    return build_enhanced_embeddings(chunks)


# -----------------------------
# Main
# -----------------------------
def main():
    """Enhanced main function with configurable vector store support."""
    load_dotenv()
    
    # Validate dependencies and configuration
    if not validate_dependencies():
        return
    
    print("🚀 Starting Enhanced Multimodal RAG Setup...")
    print(f"📊 Configuration:")
    print(f"   • Vector Store: {config.VECTOR_STORE}")
    if config.VECTOR_STORE == 'faiss':
        print(f"   • FAISS Index Type: {config.FAISS_INDEX_TYPE}")
    print(f"   • Embedding Model: {config.EMBEDDING_MODEL_NAME}")
    print(f"   • Batch Size: {config.BATCH_SIZE}")
    
    try:
        # Step 1: Prepare directories
        ensure_dirs()
        
        # Step 2: Parse PDFs
        print("\n" + "="*60)
        markdowns = parse_pdfs()
        if not markdowns:
            print("❌ No PDFs processed. Check PDF_FOLDER path and contents.")
            return
        
        # Step 3: Smart chunking
        print("\n" + "="*60)
        chunks = smart_chunk_markdowns(markdowns, max_tokens=800, overlap_tokens=100)
        if not chunks:
            print("❌ No chunks created. Check markdown processing.")
            return
        
        # Step 4: Build embeddings
        print("\n" + "="*60)
        vector_store = build_enhanced_embeddings(chunks)
        if not vector_store:
            print("❌ Failed to create embeddings.")
            return
        
        # Step 5: Test retrieval
        print("\n" + "="*60)
        print("🧪 Testing retrieval system...")
        
        # Test with different types of queries
        test_queries = [
            "installation procedure",
            "maintenance schedule", 
            "troubleshooting",
            "technical specifications"
        ]
        
        for query in test_queries:
            test_retrieval(vector_store, query, n_results=3)
            
        # Step 6: Test equipment filtering (FAISS only)
        if config.VECTOR_STORE == 'faiss':
            print("\n" + "="*60)
            print("🏭 Testing equipment filtering...")
            
            # Show available equipment
            get_available_equipment()
            
            # Test equipment-specific queries
            equipment_tests = [
                ("pump maintenance", {"make": "Flygt"}),
                ("flow meter calibration", {"equipment_type": "Flow Meter"}),
                ("installation steps", {"make": "ATC"}),
                ("control system setup", {"equipment_type": "Control System"}),
            ]
            
            for query, equipment_filter in equipment_tests:
                test_equipment_filtering(vector_store, query, equipment_filter, n_results=2)
                print("-" * 40)
        
        print(f"\n🎉 Enhanced Setup Complete! Your multimodal RAG system is ready with:")
        print(f"   ✅ Smart semantic chunking with overlap")
        print(f"   ✅ Proper token counting")
        print(f"   ✅ Rich metadata for better filtering")
        print(f"   ✅ {config.VECTOR_STORE.upper()} vector store")
        if config.VECTOR_STORE == 'faiss':
            print(f"   ✅ {config.FAISS_INDEX_TYPE.upper()} FAISS index type")
        print(f"   ✅ Enhanced retrieval testing")
        print(f"   📊 Total chunks: {len(chunks)}")
        
        # 🆕 Show file summary
        print(f"\n📁 Generated Files Summary:")
        list_vector_store_files()
        
        # 🆕 FAISS metadata inspection
        if config.VECTOR_STORE == 'faiss':
            print(f"\n🔍 FAISS Metadata Inspection:")
            inspect_faiss_metadata()
        
    except Exception as e:
        print(f"❌ Error during setup: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
