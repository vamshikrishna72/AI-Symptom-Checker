import streamlit as st
import google.generativeai as genai
import PyPDF2
from io import BytesIO
from PIL import Image
import os

# Configure API Key
api_key = "AIzaSyDZ7RfQVeokbqHyp9YE5odUL_bJMa4jVHA"
genai.configure(api_key=api_key)

# Streamlit Page Config
st.set_page_config(
    page_title="MediScan Pro - AI Health Diagnostics",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Premium Medical Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Inter', sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.stApp {
    background: linear-gradient(152deg, #0B0C13 0%, #161A28 50%, #0B0C13 100%);
    color: #FFFFFF;
}

.header-container {
    background: rgba(11, 12, 19, 0.9);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 2rem;
    margin: 2rem auto;
    border: 2px solid rgba(99, 102, 241, 0.2);
    box-shadow: 0 0 25px rgba(99, 102, 241, 0.15);
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.5rem;
    margin: 3rem 0;
}

.feature-card {
    background: rgba(17, 19, 28, 0.8);
    border: 2px solid rgba(99, 102, 241, 0.2);
    border-radius: 20px;
    padding: 2rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    backdrop-filter: blur(8px);
}

.feature-card:hover {
    transform: translateY(-5px);
    background: rgba(22, 24, 35, 0.9);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
}

.chat-container {
    background: rgba(17, 19, 28, 0.8);
    border-radius: 24px;
    padding: 2rem;
    margin: 2rem 0;
    border: 2px solid rgba(99, 102, 241, 0.2);
    backdrop-filter: blur(8px);
    min-height: 60vh;
}

.user-message {
    background: linear-gradient(135deg, #1d4ed8, #3b82f6);
    color: white;
    padding: 1.5rem;
    border-radius: 20px 20px 4px 20px;
    margin: 1rem 0 1rem auto;
    max-width: 75%;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.bot-message {
    background: linear-gradient(135deg, #6d28d9, #9333ea);
    color: white;
    padding: 1.5rem;
    border-radius: 20px 20px 20px 4px;
    margin: 1rem 0;
    max-width: 75%;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.stChatInput > div > div input {
    background: rgba(17, 19, 28, 0.9) !important;
    color: white !important;
    border: 2px solid rgba(99, 102, 241, 0.3) !important;
    border-radius: 1px !important;
    padding: 1rem 1.5rem !important;
    backdrop-filter: blur(8px) !important;
}

.stChatInput > div > div input::placeholder {
    color: #94A3B8 !important;
    opacity: 0.1 !important;
}

.typing-indicator {
    display: flex;
    align-items: center;
    padding: 1rem;
    color: #94A3B8;
    font-style: italic;
}

.dot-animation {
    display: inline-flex;
    margin-left: 8px;
}

.dot {
    width: 6px;
    height: 6px;
    background: #818CF8;
    border-radius: 50%;
    margin: 0 2px;
    animation: bounce 1.4s infinite ease-in-out;
}

@keyframes bounce {
    0%, 80%, 100% { transform: translateY(0); }
    40% { transform: translateY(-8px); }
}

.gradient-text {
    background: linear-gradient(135deg, #818CF8 0%, #4F46E5 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div style="text-align: center;">
        <h1 style="font-size: 3.5rem; margin: 0;">
            <span class="gradient-text">MediScan Pro</span>
            <span style="margin-left: 0.5rem;">🌡️</span>
        </h1>
    </div>
""", unsafe_allow_html=True)

# Center the image using columns
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    try:
        image = Image.open("screenshots/piclumen-1745416902719.png")
        st.image(image, width=300, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")

st.markdown("""
    <div style="text-align: center;">
        <p style="color: #94A3B8; font-size: 1.2rem; letter-spacing: 0.5px;">
            Advanced AI-Powered Medical Diagnostics & Report Analysis
        </p>
    </div>
""", unsafe_allow_html=True)

# File Upload Section with Enhanced Error Handling
st.markdown("""
    <div style="margin-top: 2rem;">
        <h2 style="color: #94A3B8; font-size: 1.5rem;">📄 Upload Medical Report</h2>
    </div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Medical Report (PDF/TXT)", type=["pdf", "txt"])

if uploaded_file:
    try:
        # Create a spinner to show processing status
        with st.spinner("🔍 Analyzing your medical report..."):
            # Extract text based on file type
            if uploaded_file.type == "application/pdf":
                pdf_reader = PyPDF2.PdfReader(BytesIO(uploaded_file.read()))
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            else:
                text = uploaded_file.read().decode("utf-8")

            # Create analysis prompt
            system_prompt = """As a medical expert, analyze this report and provide:
1. 🏥 Primary Findings
   - Key observations
   - Critical values
   - Abnormal results

2. 📊 Detailed Analysis
   - Interpretation of results
   - Comparison with normal ranges
   - Potential implications

3. ⚠️ Areas of Concern
   - Highlight any critical values
   - Note any significant deviations
   - Flag items requiring immediate attention

4. 💡 Recommendations
   - Suggested follow-up actions
   - Lifestyle modifications if applicable
   - Additional tests if needed

Medical Report Text:
"""
            full_prompt = system_prompt + text

            # Get analysis from Gemini
            response = st.session_state.chat_session.send_message(full_prompt)
            
            # Display analysis in a structured format
            st.markdown("""
                <div style="background: rgba(17, 19, 28, 0.8); padding: 2rem; border-radius: 15px; border: 1px solid rgba(99, 102, 241, 0.2);">
                    <h3 style="color: #818CF8;">📋 Analysis Results</h3>
                """, unsafe_allow_html=True)
            
            st.markdown(response.text)
            
            st.markdown("</div>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        st.info("Please ensure your file is not corrupted and try again.")

# Feature Grid
st.markdown("""
<div class="feature-grid">
    <div class="feature-card">
        <div style="margin-bottom: 1rem; font-size: 2rem;">🩺</div>
        <h3>Clinical Analysis</h3>
        <p style="color: #94A3B8;">Advanced symptom pattern recognition</p>
    </div>
    <div class="feature-card">
        <div style="margin-bottom: 1rem; font-size: 2rem;">📄</div>
        <h3>Report Analysis</h3>
        <p style="color: #94A3B8;">Comprehensive medical report evaluation</p>
    </div>
    <div class="feature-card">
        <div style="margin-bottom: 1rem; font-size: 2rem;">📊</div>
        <h3>Health Insights</h3>
        <p style="color: #94A3B8;">Personalized health recommendations</p>
    </div>
    <div class="feature-card">
        <div style="margin-bottom: 1rem; font-size: 2rem;">🔒</div>
        <h3>Secure Platform</h3>
        <p style="color: #94A3B8;">Encrypted data protection</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Chat Container
chat_container = st.container()
with chat_container:
    st.markdown('', unsafe_allow_html=True)

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'''
            <div class="user-message">
                <div style="font-weight: 500; margin-bottom: 0.5rem;">👤 You</div>
                {msg["content"]}
            </div>
            ''', unsafe_allow_html=True)
        else:
            st.markdown(f'''
            <div class="bot-message">
                <div style="font-weight: 500; margin-bottom: 0.5rem;">🌡️ MediScan</div>
                {msg["content"]}
            
            ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Model Configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config
)

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Chat Input Logic
if prompt := st.chat_input("Describe symptoms or ask about your report..."):
    if not st.session_state.messages:
        prompt = """You are a medical expert. Respond with:
1. 🔍 Possible Conditions
2. 📋 Diagnostic Suggestions
3. ⚠️ Red Flags
4. ✅ Next Steps
—""" + prompt

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner(""):
        with chat_container:
            # Show typing indicator
            st.markdown('''
            <div class="typing-indicator">
                Analyzing query
                <div class="dot-animation">
                    <div class="dot"></div>
                    <div class="dot"></div>
                    <div class="dot"></div>
                </div>
            </div>
            ''', unsafe_allow_html=True)
            
            # Get response
            response = st.session_state.chat_session.send_message(prompt)
            st.session_state.messages.append({
                "role": "assistant",
                "content": response.text
            })
            st.rerun()


