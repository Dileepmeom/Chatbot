"""
Equipment Maintenance Chatbot - Backend Module
============================================
This module contains all backend logic including:
- FAISS vector store management
- Document retrieval and processing
- Session management
- Equipment filtering
- LLM interaction

Author: Equipment Maintenance Team
Version: 5.0
Date: October 2025
"""

import json
import pickle
import numpy as np
import faiss
import os
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

from langchain.docstore.document import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from config import CHROMA_DB_DIR as CONFIG_CHROMA_DB_DIR

# Load environment variables
load_dotenv()


class SessionManager:
    """Manages chat sessions with persistence to disk."""
    
    def __init__(self, storage_path: str = "pdf_chat_sessions"):
        """Initialize session manager with storage path."""
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(exist_ok=True)
    
    def save_session(self, session_id: str, messages: List[Dict]) -> bool:
        """Save session to disk."""
        try:
            session_data = {
                'id': session_id,
                'messages': messages,
                'timestamp': datetime.now().isoformat(),
                'message_count': len(messages)
            }
            
            session_file = self.storage_path / f"{session_id}.json"
            with open(session_file, 'w', encoding='utf-8') as f:
                json.dump(session_data, f, ensure_ascii=False, indent=2)
            
            return True
        except Exception as e:
            print(f"Error saving session {session_id}: {e}")
            return False
    
    def load_sessions(self) -> List[Dict]:
        """Load all sessions sorted by timestamp (newest first)."""
        sessions = []
        try:
            for session_file in self.storage_path.glob("*.json"):
                try:
                    with open(session_file, 'r', encoding='utf-8') as f:
                        session_data = json.load(f)
                        sessions.append(session_data)
                except Exception as e:
                    print(f"Error loading session {session_file}: {e}")
                    continue
            
            # Sort by timestamp (newest first)
            sessions.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
            return sessions
        except Exception as e:
            print(f"Error loading sessions: {e}")
            return []
    
    def delete_session(self, session_id: str) -> bool:
        """Delete a specific session."""
        try:
            session_file = self.storage_path / f"{session_id}.json"
            if session_file.exists():
                session_file.unlink()
                return True
            return False
        except Exception as e:
            print(f"Error deleting session {session_id}: {e}")
            return False


class FAISSRetriever:
    """FAISS-based document retriever with equipment filtering - same as V4.2 EquipmentAwareFAISSRetriever"""
    
    def __init__(self, index_path: str = None, metadata_path: str = None, embeddings=None, k: int = 3):
        """Initialize FAISS retriever with paths."""
        self.index_path = index_path or str(Path(CONFIG_CHROMA_DB_DIR) / "faiss_index")
        self.metadata_path = metadata_path or str(Path(CONFIG_CHROMA_DB_DIR) / "faiss_metadata_v3.pkl")
        
        self.embeddings = embeddings or OpenAIEmbeddings(model="text-embedding-3-small")
        self.index = None
        self.metadata_store = []  # V4.2 uses list, not dict
        self.k = k
        
        # Load index and metadata
        self._load_from_disk()
    
    def _load_from_disk(self) -> None:
        """Load FAISS index and metadata from disk - same as V4.2"""
        try:
            # Load FAISS index
            self.index = faiss.read_index(self.index_path)
            
            # Load metadata
            with open(self.metadata_path, 'rb') as f:
                data = pickle.load(f)
                self.metadata_store = data['metadata_store']
                
        except Exception as e:
            raise Exception(f"Error loading FAISS: {str(e)}")
    
    def get_available_equipment(self) -> Dict[str, List[str]]:
        """Extract available equipment types, makes, and models from metadata - same as V4.2"""
        equipment_types = set()
        makes = set()
        models = set()
        
        for metadata in self.metadata_store:
            equipment_types.add(metadata.get('equipment_type', 'Unknown'))
            makes.add(metadata.get('make', 'Unknown'))
            models.add(metadata.get('model', 'Unknown'))
        
        return {
            'equipment_types': sorted([eq for eq in equipment_types if eq != 'Unknown']),
            'makes': sorted([make for make in makes if make != 'Unknown']),
            'models': sorted([model for model in models if model != 'Unknown'])
        }
    
    def get_relevant_documents(self, query: str, equipment_filter: Dict[str, str] = None) -> List[Document]:
        """Get relevant documents for a query with optional equipment filtering - same as V4.2"""
        try:
            # Get a larger initial search for filtering
            search_k = self.k * 3 if equipment_filter else self.k
            
            # Generate query embedding
            query_embedding = self.embeddings.embed_query(query)
            query_vector = np.array([query_embedding], dtype=np.float32)
            faiss.normalize_L2(query_vector)
            
            # Search
            scores, indices = self.index.search(query_vector, search_k)
            
            # Prepare results in LangChain Document format
            documents = []
            
            for score, idx in zip(scores[0], indices[0]):
                if idx >= 0 and idx < len(self.metadata_store):
                    metadata = self.metadata_store[idx]
                    
                    # Apply equipment filter if provided
                    if equipment_filter:
                        match = True
                        for filter_key, filter_value in equipment_filter.items():
                            if filter_value and filter_value != "All":
                                metadata_value = metadata.get(filter_key, '')
                                if filter_value.lower() not in metadata_value.lower():
                                    match = False
                                    break
                        if not match:
                            continue
                    
                    # Create a proper LangChain Document with enhanced metadata
                    doc = Document(
                        page_content=metadata['text'],
                        metadata={
                            'pages': ','.join(map(str, metadata['pages'])),
                            'page_count': metadata['page_count'],
                            'heading': metadata['heading'],
                            'source_file': metadata['source_file'],
                            'chunk_index': metadata['chunk_index'],
                            'token_count': metadata['token_count'],
                            'has_tables': metadata['has_tables'],
                            'has_figures': metadata['has_figures'],
                            'content_type': metadata['content_type'],
                            'text_length': metadata['text_length'],
                            'is_technical': metadata['is_technical'],
                            'similarity_score': float(score),
                            'page_number': metadata['pages'][0] if metadata['pages'] else 'N/A',
                            # Equipment metadata
                            'equipment_type': metadata.get('equipment_type', 'Unknown'),
                            'make': metadata.get('make', 'Unknown'),
                            'model': metadata.get('model', 'Unknown'),
                            'equipment_filename': metadata.get('equipment_filename', '')
                        }
                    )
                    
                    documents.append(doc)
                    
                    # Stop when we have enough documents
                    if len(documents) >= self.k:
                        break
            
            return documents
            
        except Exception as e:
            print(f"Error during FAISS query: {str(e)}")
            return []


class EquipmentChatbot:
    """Main chatbot class that orchestrates retrieval and response generation."""
    
    def __init__(self):
        """Initialize the chatbot with retriever and LLM - same as V4.2 load_vectorstore logic."""
        # Get OpenAI API key
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        if not OPENAI_API_KEY:
            raise Exception("No OpenAI API key found in environment variables")
        
        # FAISS paths (matching rag_setup_V4.py configuration)
        VECTOR_STORE_DIR = Path(CONFIG_CHROMA_DB_DIR)
        FAISS_INDEX_PATH = VECTOR_STORE_DIR / "faiss_index"
        FAISS_METADATA_PATH = VECTOR_STORE_DIR / "faiss_metadata_v3.pkl"
        
        # Check if files exist
        if not FAISS_INDEX_PATH.exists() or not FAISS_METADATA_PATH.exists():
            raise Exception(f"FAISS index or metadata not found. Run rag_setup_V4.py first.")
        
        # Initialize OpenAI embeddings (same as used during indexing)
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY, model="text-embedding-3-small")
        
        # Create enhanced FAISS retriever
        self.retriever = FAISSRetriever(
            index_path=str(FAISS_INDEX_PATH),
            metadata_path=str(FAISS_METADATA_PATH),
            embeddings=embeddings,
            k=3  # Default value, will be updated by slider
        )
        
        self.session_manager = SessionManager()
        
        # Initialize LLM (using Ollama llama3.1 model - same as V4.2)
        self.llm = ChatOllama(model="llama3.1", temperature=0.1)
        
        # Create prompt template (exact same as V4.2)
        self.equipment_aware_template = """
You are a specialized technical maintenance assistant with expertise in industrial equipment.

Answer the question using ONLY the provided context from the equipment documentation. 
Be specific and include relevant details like:
- Step-by-step procedures with numbers
- Part numbers and specifications
- Safety warnings and precautions
- Page references when available
- Equipment-specific technical details

If you reference procedures, mention the page numbers when available.
If the answer is not in the provided context, say "I don't know - this information is not available in the provided documentation."

Context (delimited by triple backticks):
```\n{context}\n```

Question: {question}

Answer:
"""
        self.prompt_template = ChatPromptTemplate.from_template(self.equipment_aware_template)
    
    def get_response(self, query: str, equipment_filter: Dict = None, 
                    temperature: float = 0.1, top_k: int = 3, 
                    min_similarity: float = 0.6) -> Dict[str, Any]:
        """Generate response to user query with context retrieval - same logic as V4.2."""
        try:
            # Update retriever k value if needed
            if hasattr(self.retriever, 'k'):
                if self.retriever.k != top_k:
                    self.retriever.k = top_k
            
            # Get relevant documents with equipment filtering (same as V4.2)
            docs = self.retriever.get_relevant_documents(query, equipment_filter)
            
            if not docs:
                filter_info = f" matching your equipment filters ({equipment_filter})" if equipment_filter else ""
                return {
                    'response': f"I couldn't find any relevant information{filter_info} in the equipment documentation. Try adjusting your equipment filters or rephrasing your question.",
                    'sources': [],
                    'equipment_filter': equipment_filter
                }
            
            # Prepare context (same as V4.2)
            context = "\n\n".join(doc.page_content for doc in docs)
            
            # Create a temporary LLM with the specified temperature (same as V4.2)
            temp_llm = ChatOllama(model="llama3.1", temperature=temperature)
            
            # Create chain and generate response (same approach as V4.2)
            chain = self.prompt_template | temp_llm
            response = chain.invoke({"context": context, "question": query})
            
            # Prepare sources with enhanced equipment metadata and relevance filtering (same as V4.2)
            sources = []
            for doc in docs:
                metadata = doc.metadata
                similarity_score = metadata.get('similarity_score', 0.0)
                
                # Clean the text content - remove markdown headers and normalize formatting (same as V4.2)
                clean_content = doc.page_content
                # Remove markdown headers (# ## ### etc.)
                clean_content = re.sub(r'^#+\s*', '', clean_content, flags=re.MULTILINE)
                # Remove extra whitespace and normalize
                clean_content = re.sub(r'\n\s*\n', '\n\n', clean_content.strip())
                
                source_info = {
                    "page": metadata.get('pages', metadata.get('page_number', 'N/A')),
                    "heading": metadata.get('heading', 'No heading'),
                    "similarity_score": similarity_score,
                    "excerpt": clean_content[:200] + "..." if len(clean_content) > 200 else clean_content,
                    # Equipment metadata
                    "equipment_type": metadata.get('equipment_type', 'Unknown'),
                    "make": metadata.get('make', 'Unknown'),
                    "model": metadata.get('model', 'Unknown'),
                    "equipment_filename": metadata.get('equipment_filename', ''),
                    # PDF viewing info (for UI compatibility)
                    "source_file": metadata.get('source_file', 'Unknown'),
                    "page_number": metadata.get('pages', [1])[0] if metadata.get('pages') else 1
                }
                sources.append(source_info)
            
            # Filter sources based on relevance (using user settings) - same as V4.2
            def filter_relevant_sources(sources, min_similarity_threshold, max_sources):
                """Filter sources based on similarity score and limit count"""
                # Sort by similarity score (descending)
                sorted_sources = sorted(sources, key=lambda x: x['similarity_score'], reverse=True)
                
                if not sorted_sources:
                    return []
                
                # Method 1: Use user-defined threshold
                relevant_sources = [s for s in sorted_sources if s['similarity_score'] >= min_similarity_threshold]
                
                # Method 2: If no sources meet threshold, use adaptive approach
                if len(relevant_sources) == 0:
                    # Take best result and find adaptive threshold
                    best_score = sorted_sources[0]['similarity_score']
                    adaptive_threshold = max(best_score * 0.7, 0.4)
                    relevant_sources = [s for s in sorted_sources if s['similarity_score'] >= adaptive_threshold]
                    print(f"Applied adaptive threshold: {adaptive_threshold:.3f} (original: {min_similarity_threshold:.3f})")
                
                # Limit to max_sources (use default of 3 if not specified)
                return relevant_sources[:max_sources]
            
            # Apply filtering with user settings (default max_sources=3 like V4.2)
            filtered_sources = filter_relevant_sources(sources, min_similarity, 3)
            
            # Add bot response to chat with filtered sources (same as V4.2)
            if filtered_sources:
                filter_summary = ""
                if equipment_filter:
                    active_filters = [f"{k}: {v}" for k, v in equipment_filter.items()]
                    filter_summary = f"\n\n🎯 **Filtered Results** ({', '.join(active_filters)})"
                
                enhanced_content = f"{response.content if hasattr(response, 'content') else str(response)}{filter_summary}"
                
                return {
                    'response': enhanced_content,
                    'sources': filtered_sources,
                    'equipment_filter': equipment_filter,
                    'total_sources_found': len(sources),
                    'sources_shown': len(filtered_sources)
                }
            else:
                # No sources meet the relevance threshold (same as V4.2)
                filter_info = f" with equipment filters ({equipment_filter})" if equipment_filter else ""
                enhanced_content = f"{response.content if hasattr(response, 'content') else str(response)}\n\n⚠️ **Note**: Found {len(sources)} document chunks{filter_info}, but none met the minimum similarity threshold of {min_similarity:.1%}. You may want to lower the similarity threshold in the sidebar or try different equipment filters."
                
                return {
                    'response': enhanced_content,
                    'sources': [],
                    'equipment_filter': equipment_filter,
                    'total_sources_found': len(sources),
                    'sources_shown': 0
                }
            
        except Exception as e:
            return {
                'response': f"An error occurred while processing your request: {str(e)}",
                'sources': [],
                'equipment_filter': equipment_filter
            }
    
    def get_available_equipment(self) -> Dict[str, List[str]]:
        """Get available equipment from retriever."""
        return self.retriever.get_available_equipment()
    
    def save_session(self, session_id: str, messages: List[Dict]) -> bool:
        """Save chat session."""
        return self.session_manager.save_session(session_id, messages)
    
    def load_sessions(self) -> List[Dict]:
        """Load all chat sessions."""
        return self.session_manager.load_sessions()
    
    def delete_session(self, session_id: str) -> bool:
        """Delete a chat session."""
        return self.session_manager.delete_session(session_id)


# Global chatbot instance (singleton pattern)
_chatbot_instance = None

def get_chatbot() -> EquipmentChatbot:
    """Get or create the global chatbot instance."""
    global _chatbot_instance
    if _chatbot_instance is None:
        _chatbot_instance = EquipmentChatbot()
    return _chatbot_instance


# API-like functions for the frontend
def process_chat_query(query: str, equipment_filter: Dict = None, 
                      temperature: float = 0.1, top_k: int = 3, 
                      min_similarity: float = 0.6, max_sources_display: int = 3) -> Dict[str, Any]:
    """Process a chat query and return response with sources - same interface as V4.2."""
    chatbot = get_chatbot()
    return chatbot.get_response(
        query=query,
        equipment_filter=equipment_filter,
        temperature=temperature,
        top_k=top_k,
        min_similarity=min_similarity
    )

def get_equipment_options() -> Dict[str, List[str]]:
    """Get available equipment types, makes, and models."""
    chatbot = get_chatbot()
    return chatbot.get_available_equipment()

def save_chat_session(session_id: str, messages: List[Dict]) -> bool:
    """Save a chat session."""
    chatbot = get_chatbot()
    return chatbot.save_session(session_id, messages)

def load_chat_sessions() -> List[Dict]:
    """Load all chat sessions."""
    chatbot = get_chatbot()
    return chatbot.load_sessions()

def delete_chat_session(session_id: str) -> bool:
    """Delete a chat session."""
    chatbot = get_chatbot()
    return chatbot.delete_session(session_id)

def get_total_documents() -> int:
    """Get total number of documents in the index."""
    chatbot = get_chatbot()
    return len(chatbot.retriever.metadata_store)