"""
Equipment Maintenance Chatbot - Frontend UI Module
=================================================
This module contains all Streamlit UI components and user interface logic:
- Page configuration and styling
- Sidebar controls and filters
- Chat interface
- Session management UI
- Source display components

Author: Equipment Maintenance Team
Version: 5.0
Date: October 2025
"""

import streamlit as st
import base64
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

# Import backend functions
from Manual_chatbot_backend_V5 import (
    process_chat_query,
    get_equipment_options,
    save_chat_session,
    load_chat_sessions,
    delete_chat_session,
    get_total_documents
)

# PDF source directory
PDF_SOURCE_DIR = Path("C:/Dileep/13_LLM/RAG/RAG_with_Docling/multimodal_rag/multimodal_rag/docs/pdf_source")

# Page Configuration
st.set_page_config(
    page_title="🏭 Equipment Maintenance Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern UI CSS with enhanced source cards and equipment styling
st.markdown("""
    <style>
        .main { background-color: #f9fafb; }
        .stSidebar { background-color: white; border-right: 1px solid #e5e7eb; }
        
        .chat-container {
            max-width: 48rem;
            margin: 0 auto;
            padding: 1rem;
        }
        
        .message-container {
            margin: 1rem 0;
            animation: fadeIn 0.3s ease-in;
        }
        
        .user-message {
            background-color: #eff6ff;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-left: auto;
            max-width: 80%;
        }
        
        .bot-message {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            padding: 1.5rem;
            border-radius: 12px;
            margin-right: auto;
            max-width: 80%;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
            border: 1px solid #e2e8f0;
            transition: all 0.3s ease;
        }
        
        .bot-message:hover {
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        .sources-container {
            background-color: white;
            border-bottom: 1px solid #e5e7eb;
            padding: 1rem;
            margin: -1rem -1rem 1rem -1rem;
        }
        
        .source-card {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            height: 220px;
            display: flex;
            flex-direction: column;
        }
        
        .source-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        .source-card.high-relevance {
            background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
            border-color: #10b981;
            height: 220px;
        }
        
        .source-card.medium-relevance {
            background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
            border-color: #f59e0b;
            height: 220px;
        }
        
        .source-card.low-relevance {
            background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
            border-color: #64748b;
            height: 220px;
        }
        
        .source-content {
            flex: 1;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }
        
        .equipment-tag {
            display: inline-block;
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            margin-bottom: 8px;
        }
        
        .source-excerpt {
            flex: 1;
            overflow-y: auto;
            color: #374151;
            font-size: 0.875rem;
            line-height: 1.5;
            background-color: rgba(255,255,255,0.6);
            padding: 12px;
            border-radius: 8px;
            border-left: 3px solid #d1d5db;
            margin-top: auto;
        }
        
        .relevance-badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 600;
            margin-top: 4px;
        }
        
        .badge-high {
            background-color: #10b981;
            color: white;
        }
        
        .badge-medium {
            background-color: #f59e0b;
            color: white;
        }
        
        .badge-low {
            background-color: #64748b;
            color: white;
        }
        
        .equipment-filter-section {
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
            border: 2px solid #0ea5e9;
            border-radius: 16px;
            padding: 20px;
            margin: 16px 0;
            box-shadow: 0 4px 12px rgba(14, 165, 233, 0.1);
            transition: all 0.3s ease;
        }
        
        .equipment-filter-section:hover {
            box-shadow: 0 6px 20px rgba(14, 165, 233, 0.15);
        }
        
        /* Selectbox styling for equipment filters */
        .equipment-filter-section .stSelectbox > div > div {
            background: rgba(255, 255, 255, 0.9) !important;
            border: 1px solid #0ea5e9 !important;
            border-radius: 12px !important;
            transition: all 0.3s ease !important;
        }
        
        .equipment-filter-section .stSelectbox > div > div:hover {
            background: rgba(255, 255, 255, 1) !important;
            border-color: #0284c7 !important;
            box-shadow: 0 2px 8px rgba(14, 165, 233, 0.2) !important;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Custom form styling */
        .stForm {
            border: none !important;
            background: transparent !important;
        }
        
        /* Input field styling */
        .stTextInput > div > div > input {
            border-radius: 25px !important;
            padding: 12px 20px !important;
            border: 2px solid #e2e8f0 !important;
            transition: all 0.3s ease !important;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #3b82f6 !important;
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
        }
        
        /* Button styling */
        .stButton > button {
            border-radius: 20px !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
        }
        
        /* New Session Button specific styling */
        div[data-testid="stSidebar"] .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #86efac 0%, #4ade80 100%) !important;
            color: #065f46 !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 12px 20px !important;
            font-weight: 600 !important;
            width: 100% !important;
            box-shadow: 0 2px 8px rgba(134, 239, 172, 0.3) !important;
        }
        
        div[data-testid="stSidebar"] .stButton > button[kind="primary"]:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 16px rgba(134, 239, 172, 0.4) !important;
            background: linear-gradient(135deg, #bbf7d0 0%, #86efac 100%) !important;
        }
        
        /* Hide the form submit button */
        .stForm button[kind="primaryFormSubmit"] {
            display: none !important;
        }
        
        /* Scrollable sessions container */
        .sessions-container {
            max-height: 200px;
            overflow-y: auto;
            padding: 8px;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            margin-bottom: 16px;
        }
        
        .sessions-container::-webkit-scrollbar {
            width: 6px;
        }
        
        .sessions-container::-webkit-scrollbar-track {
            background: #f1f5f9;
            border-radius: 3px;
        }
        
        .sessions-container::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 3px;
        }
        
        .sessions-container::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }
        
        /* Session button styling */
        .sessions-container .stButton > button {
            width: 100% !important;
            margin-bottom: 4px !important;
            padding: 8px 12px !important;
            border-radius: 6px !important;
            background: rgba(255, 255, 255, 0.8) !important;
            border: 1px solid #e2e8f0 !important;
            color: #374151 !important;
            font-size: 0.875rem !important;
            transition: all 0.2s ease !important;
        }
        
        .sessions-container .stButton > button:hover {
            background: rgba(59, 130, 246, 0.1) !important;
            border-color: #3b82f6 !important;
            transform: translateX(2px) !important;
        }
        
        /* PDF Viewer Styles - Simplified */
        .pdf-viewer-container {
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            border-radius: 12px;
            padding: 20px;
            margin: 20px 0;
            border: 2px solid #e2e8f0;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        .pdf-controls {
            display: flex;
            gap: 12px;
            align-items: center;
            margin-bottom: 16px;
            padding: 12px;
            background: white;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
        }
        
        /* Enhanced source card styling */
        .source-card {
            position: relative !important;
            transition: all 0.3s ease !important;
        }
        
        .source-card:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15) !important;
        }
    </style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize Streamlit session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "session_id" not in st.session_state:
        st.session_state.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if "show_pdf" not in st.session_state:
        st.session_state.show_pdf = False
    
    if "pdf_file" not in st.session_state:
        st.session_state.pdf_file = None
        
    if "pdf_page" not in st.session_state:
        st.session_state.pdf_page = 1


def load_pdf_as_base64(pdf_filename: str) -> str:
    """Load PDF file and return as base64 string."""
    try:
        # Clean the filename to remove any extra path components
        clean_filename = pdf_filename.replace('\\', '').replace('/', '').strip()
        pdf_path = PDF_SOURCE_DIR / clean_filename
        
        if pdf_path.exists():
            with open(pdf_path, "rb") as pdf_file:
                pdf_bytes = pdf_file.read()
                pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
                return pdf_base64
        else:
            st.error(f"PDF file not found: {clean_filename}")
            return None
    except Exception as e:
        st.error(f"Error loading PDF {pdf_filename}: {str(e)}")
        return None


def render_pdf_modal():
    """Render PDF modal dialog if PDF viewing is requested."""
    if st.session_state.show_pdf and st.session_state.pdf_file:
        try:
            # Create modal container
            modal = st.container()
            
            with modal:
                # Modal header
                col1, col2 = st.columns([6, 1])
                with col1:
                    st.markdown(f"### 📄 PDF Viewer: {st.session_state.pdf_file}")
                    st.markdown(f"**Page:** {st.session_state.pdf_page}")
                
                with col2:
                    if st.button("✕ Close", key="close_pdf", help="Close PDF viewer"):
                        st.session_state.show_pdf = False
                        st.session_state.pdf_file = None
                        st.session_state.pdf_page = 1
                        st.rerun()
                
                # Load and display PDF
                pdf_base64 = load_pdf_as_base64(st.session_state.pdf_file)
                
                if pdf_base64:
                    # Display PDF info
                    st.info(f"📄 Displaying: {st.session_state.pdf_file} (Page {st.session_state.pdf_page})")
                    
                    # Create PDF viewer with page navigation
                    pdf_html = f"""
                    <div style="width: 100%; height: 600px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; background: #f5f5f5;">
                        <iframe 
                            src="data:application/pdf;base64,{pdf_base64}#page={st.session_state.pdf_page}&zoom=page-width"
                            width="100%" 
                            height="100%" 
                            style="border: none;">
                            <div style="padding: 20px; text-align: center;">
                                <p>Your browser does not support embedded PDFs.</p>
                                <a href="data:application/pdf;base64,{pdf_base64}" download="{st.session_state.pdf_file}" 
                                   style="background: #3b82f6; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
                                   📥 Download PDF
                                </a>
                            </div>
                        </iframe>
                    </div>
                    """
                    
                    st.markdown(pdf_html, unsafe_allow_html=True)
                    
                    # Alternative: Provide download option
                    st.download_button(
                        label="📥 Download PDF",
                        data=base64.b64decode(pdf_base64),
                        file_name=st.session_state.pdf_file,
                        mime="application/pdf",
                        help="Download the PDF file to view it locally"
                    )
                    
                    # Navigation controls
                    st.markdown("---")
                    col1, col2, col3 = st.columns([1, 2, 1])
                    
                    with col1:
                        if st.button("← Previous Page", key="prev_page") and st.session_state.pdf_page > 1:
                            st.session_state.pdf_page -= 1
                            st.rerun()
                    
                    with col2:
                        new_page = st.number_input(
                            "Go to page:", 
                            min_value=1, 
                            value=st.session_state.pdf_page,
                            key="page_input"
                        )
                        if new_page != st.session_state.pdf_page:
                            st.session_state.pdf_page = new_page
                            st.rerun()
                    
                    with col3:
                        if st.button("Next Page →", key="next_page"):
                            st.session_state.pdf_page += 1
                            st.rerun()
                else:
                    st.error("Unable to load PDF file")
            
            # Add some spacing
            st.markdown("---")
            
        except Exception as e:
            st.error(f"Error rendering PDF modal: {str(e)}")
            st.exception(e)


def render_sidebar() -> Dict[str, Any]:
    """Render the sidebar with equipment filters and session management."""
    with st.sidebar:
        st.title("🏭 Equipment Maintenance")
        st.markdown("AI Assistant with Equipment Filtering")
        
        # Get available equipment options
        try:
            available_equipment = get_equipment_options()
        except Exception as e:
            st.error(f"Error loading equipment options: {e}")
            available_equipment = {}
        
        # Equipment Filtering Section
        equipment_filter = {}
        if available_equipment:
            #st.markdown('<div class="equipment-filter-section">', unsafe_allow_html=True)
            st.markdown("### 🏭 **Equipment Filtering**")
            
            # Equipment Type Dropdown
            equipment_type_options = ["All"] + available_equipment.get('equipment_types', [])
            selected_equipment_type = st.selectbox(
                "🔧 Equipment Type",
                equipment_type_options,
                help="Filter by equipment type for more accurate results"
            )
            
            # Make Dropdown  
            make_options = ["All"] + available_equipment.get('makes', [])
            selected_make = st.selectbox(
                "🏭 Manufacturer",
                make_options,
                help="Filter by equipment manufacturer"
            )
            
            # Model Dropdown
            model_options = ["All"] + available_equipment.get('models', [])
            selected_model = st.selectbox(
                "📋 Model",
                model_options,
                help="Filter by specific equipment model"
            )
            
            # Show current filter status
            if any([selected_equipment_type != "All", selected_make != "All", selected_model != "All"]):
                st.markdown("**🎯 Active Filters:**")
                if selected_equipment_type != "All":
                    st.markdown(f"• Type: `{selected_equipment_type}`")
                if selected_make != "All":
                    st.markdown(f"• Make: `{selected_make}`")
                if selected_model != "All":
                    st.markdown(f"• Model: `{selected_model}`")
            else:
                st.markdown("**🌐 Searching all equipment**")
                
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Build equipment filter
            if selected_equipment_type != "All":
                equipment_filter['equipment_type'] = selected_equipment_type
            if selected_make != "All":
                equipment_filter['make'] = selected_make
            if selected_model != "All":
                equipment_filter['model'] = selected_model
        
        st.markdown("---")
        
        # New Session Button
        if st.button("🆕 New Session", key="new_session", use_container_width=True, type="primary"):
            st.session_state.messages = []
            st.session_state.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
            st.rerun()
        
        # Previous Sessions
        render_session_management()
        
        st.markdown("---")
        
        # Settings
        settings = render_settings()
        
        return {
            'equipment_filter': equipment_filter,
            'settings': settings
        }


def render_session_management():
    """Render the session management section."""
    st.subheader("💾 Previous Sessions")
    
    try:
        sessions = load_chat_sessions()
    except Exception as e:
        st.error(f"Error loading sessions: {e}")
        sessions = []
    
    if sessions:
        # Create scrollable container for sessions
        st.markdown('<div class="sessions-container">', unsafe_allow_html=True)
        
        # Show up to 10 sessions in scrollable area
        for i, session in enumerate(sessions[:5]):
            session_label = f"📋 {session['id']} ({session['timestamp'][:10]})"
            if st.button(session_label, key=f"session_{i}"):
                st.session_state.session_id = session['id']
                st.session_state.messages = session['messages']
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Show session count info
        if len(sessions) > 10:
            st.caption(f"Showing 10 of {len(sessions)} sessions (scroll to see more)")
        else:
            st.caption(f"{len(sessions)} session{'s' if len(sessions) != 1 else ''} available")
    else:
        st.info("No previous sessions found. Start chatting to create your first session!")


def render_settings() -> Dict[str, Any]:
    """Render the settings section and return settings values."""
    st.subheader("⚙️ Settings")
    
    temperature = st.slider(
        "Temperature", 
        0.0, 1.0, 0.1, 
        help="Higher = more creative, lower = more factual"
    )
    
    top_k = st.slider(
        "Top K Chunks", 
        1, 10, 3, 
        help="How many chunks to retrieve from the index"
    )
    
    # Source filtering settings
    st.markdown("**🔍 Source Filtering**")
    min_similarity = st.slider(
        "Minimum Similarity", 
        0.0, 1.0, 0.6, 0.05,
        help="Minimum similarity score to show a source (0.6 = 60% similarity)"
    )
    
    max_sources_display = st.selectbox(
        "Max Sources to Display", 
        [1, 2, 3, 4, 5], 
        index=2,  # Default to 3
        help="Maximum number of relevant sources to display"
    )
    
    return {
        'temperature': temperature,
        'top_k': top_k,
        'min_similarity': min_similarity,
        'max_sources_display': max_sources_display
    }


def render_welcome_message():
    """Render the welcome message when no messages exist."""
    welcome_content = f"""
        <div style="background: linear-gradient(135deg, #e0f2fe 0%, #b3e5fc 100%); 
                   padding: 2rem; border-radius: 16px; margin: 2rem 0; 
                   border: 2px solid #0288d1; text-align: center;">
            <h3 style="color: #0c4a6e; margin-bottom: 1rem;">🏭 Welcome to the Equipment Maintenance Assistant!</h3>
            <p style="color: #075985; margin-bottom: 1rem;">
                Ask me anything about:<br>
                • Installation procedures<br>
                • Maintenance schedules<br>
                • Troubleshooting guides<br>
                • Technical specifications
            </p>
        </div>
    """
    st.markdown(welcome_content, unsafe_allow_html=True)


def render_source_card_in_column(source: Dict, col):
    """Render a single source card in a Streamlit column with PDF viewer functionality."""
    with col:
        # Determine relevance class (same thresholds as V4.2)
        score = source.get('similarity_score', 0.0)
        if score >= 0.8:
            relevance_class = "high-relevance"
            badge_class = "badge-high"
            relevance_text = "High"
        elif score >= 0.6:  # V4.2 uses 0.6, not 0.65
            relevance_class = "medium-relevance"
            badge_class = "badge-medium"
            relevance_text = "Medium"
        else:
            relevance_class = "low-relevance"
            badge_class = "badge-low"
            relevance_text = "Low"
        
        # Equipment information (same format as V4.2)
        equipment_info = f"{source.get('make', 'Unknown')} {source.get('model', 'Unknown')}"
        equipment_type = source.get('equipment_type', 'Unknown')
        
        # Create unique key for this source card
        card_key = f"pdf_btn_{hash(str(source))}"
        
        # Source card content (exactly same as V4.2)
        st.markdown(f"""
            <div class="source-card {relevance_class}">
                <div class="source-content">
                    <div class="equipment-tag">
                        🏭 {equipment_info} ({equipment_type})
                    </div>
                    <div style="font-weight: 600; color: #1f2937; margin-bottom: 8px;">
                        📄 {source.get('heading', 'No heading')}
                    </div>
                    <div style="font-size: 0.875rem; color: #6b7280; margin-bottom: 8px;">
                        Page: {source.get('page', 'N/A')} • 
                        Similarity: {score:.1%}
                    </div>
                    <div class="source-excerpt">
                        {source.get('excerpt', 'No excerpt available')}
                    </div>
                    <div class="relevance-badge {badge_class}">
                        {relevance_text} Relevance
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # PDF viewer button - use equipment_filename and page from source
        pdf_file = source.get('equipment_filename', source.get('source_file', 'Unknown'))
        page_number = source.get('page_number', 1)
        if st.button(f"📄 View PDF", key=card_key, help=f"Open {pdf_file} at page {page_number}"):
            st.session_state.show_pdf = True
            st.session_state.pdf_file = pdf_file
            st.session_state.pdf_page = page_number
            st.rerun()


def render_chat_interface():
    """Render the main chat interface."""
    # Display chat messages
    with st.container():
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        if not st.session_state.messages:
            render_welcome_message()
        
        for message in st.session_state.messages:
            with st.container():
                if message["role"] == "user":
                    st.markdown(f"""
                        <div class="message-container">
                            <div class="user-message">
                                <strong>🤔 You:</strong> {message["content"]}
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    # Display bot message first (same format as V4.2)
                    st.markdown(f"""
                        <div class="message-container">
                            <div class="bot-message">
                                <strong style="color: #1f2937;">🤖 Assistant:</strong>
                                <div style="margin-top: 8px; color: #374151; line-height: 1.6;">
                                    {message["content"]}
                                </div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Display sources below the bot response if available (same as V4.2)
                    if "sources" in message and message["sources"]:
                        st.markdown("#### 📚 **Sources & References**")
                        
                        # Create columns for source cards (same as V4.2)
                        cols = st.columns(max(len(message["sources"]), 1))
                        
                        for idx, source in enumerate(message["sources"]):
                            render_source_card_in_column(source, cols[idx % len(cols)])
        
        st.markdown('</div>', unsafe_allow_html=True)


def render_chat_input(sidebar_data: Dict) -> None:
    """Render the chat input form."""
    # Create a form to handle Enter key submission
    with st.form(key="chat_form", clear_on_submit=True, border=False):
        user_input = st.text_input(
            "Ask about equipment maintenance, installation, or troubleshooting...", 
            key="user_input",
            placeholder="Type your question and press Enter to submit",
            help="💡 Tip: Use equipment filters in sidebar for targeted results!"
        )
        
        # Hidden submit button to enable Enter key submission
        submit_button = st.form_submit_button("Submit")

    # Query handling - triggers when form is submitted (Enter key or submit button)
    if submit_button and user_input.strip():
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": user_input.strip()})
        
        # Show processing indicator
        with st.spinner("🔍 Searching equipment documentation and generating response..."):
            # Get response from backend
            response_data = process_chat_query(
                query=user_input.strip(),
                equipment_filter=sidebar_data['equipment_filter'],
                temperature=sidebar_data['settings']['temperature'],
                top_k=sidebar_data['settings']['top_k'],
                min_similarity=sidebar_data['settings']['min_similarity']
            )
            
            # Limit sources for display
            max_sources = sidebar_data['settings']['max_sources_display']
            limited_sources = response_data['sources'][:max_sources]
            
            # Add bot response to chat
            bot_message = {
                "role": "assistant", 
                "content": response_data['response'],
                "sources": limited_sources
            }
            st.session_state.messages.append(bot_message)
            
            # Save session
            try:
                save_chat_session(st.session_state.session_id, st.session_state.messages)
            except Exception as e:
                st.error(f"Error saving session: {e}")
        
        # Rerun to show new messages
        st.rerun()


def main():
    """Main application function."""
    try:
        # Initialize session state
        initialize_session_state()
        
        # Check if PDF modal should be shown
        if st.session_state.show_pdf:
            render_pdf_modal()
            return  # Don't render the rest of the UI when PDF is open
        
        # Main page title
        st.title("🏭 Equipment Maintenance Assistant")
        st.markdown("*AI-powered support for industrial equipment documentation*")
        
        # Render sidebar and get configuration
        sidebar_data = render_sidebar()
        
        # Render main chat interface
        render_chat_interface()
        
        # Render chat input
        render_chat_input(sidebar_data)
        
    except Exception as e:
        st.error(f"Application error: {str(e)}")
        st.exception(e)


if __name__ == "__main__":
    main()