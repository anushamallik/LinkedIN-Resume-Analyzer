import streamlit as st
import tempfile
from backend.resume_parser import extract_text_from_pdf
from backend.job_parser import extract_job_description
from backend.match_engine import compute_similarity
from backend.suggestions import generate_resume_tips
from backend.utils import clean_text

# ----------------- INIT CONFIG --------------------
st.set_page_config(page_title="LinkedIn Resume Analyzer", page_icon="📄", layout="centered")

# ----------------- SIDEBAR SETTINGS ----------------
with st.sidebar:
    st.title("⚙️ Settings")
    
    st.session_state.dark_mode = st.checkbox("🌙 Dark Mode", value=st.session_state.get("dark_mode", False))
    st.session_state.font_size = st.slider("🔠 Font Size", 14, 24, 16)
    st.session_state.accent_color = st.color_picker("🎨 Accent Color", "#4a90e2")
    st.session_state.detailed = st.radio("📝 Output Mode", ["Match Score", "Full Analysis"])
    
    if st.button("🔄 Reset All"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# ----------------- DYNAMIC STYLES -----------------
def apply_custom_styles():
    css = f"""
    <style>
        html, body, .stApp {{
            font-size: {st.session_state.font_size}px;
            background-color: {'#0e1117' if st.session_state.dark_mode else '#ffffff'};
            color: {'#FAFAFA' if st.session_state.dark_mode else '#000000'};
        }}
        .stTextArea textarea, .stTextInput input {{
            background-color: {'#262730' if st.session_state.dark_mode else '#ffffff'};
            color: {'#FAFAFA' if st.session_state.dark_mode else '#000000'};
        }}
        .stButton>button {{
            background-color: {st.session_state.accent_color};
            color: white;
        }}
        .stFileUploader, .stMarkdown, .stSubheader {{
            color: {'#FAFAFA' if st.session_state.dark_mode else '#000000'};
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

apply_custom_styles()

# ----------------- MAIN UI -----------------
st.title("📄 LinkedIn Resume Analyzer")
st.markdown("Upload your resume and paste a job description to see how well you match and get personalized suggestions!")

resume_file = st.file_uploader("📁 Upload Your Resume (PDF)", type=["pdf"])
job_text = st.text_area("🧾 Paste Job Description Here", height=200)

# ----------------- ANALYSIS -----------------
if st.button("🔍 Analyze"):
    if not resume_file or not job_text.strip():
        st.error("Please upload a resume and paste a job description.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(resume_file.read())
            resume_text = extract_text_from_pdf(tmp.name)

        resume_text = clean_text(resume_text)
        job_text_clean = clean_text(job_text)

        with st.spinner("Analyzing..."):
            match_score = compute_similarity(resume_text, job_text_clean)
            suggestions = generate_resume_tips(resume_text, job_text_clean)

        st.subheader("🎯 Match Score")
        st.progress(int(match_score))
        st.success(f"✅ Your resume matches **{match_score}%** of the job description.")

        if st.session_state.detailed == "Full Analysis":
            st.subheader("💡 Improvement Suggestions")
            st.markdown(
                f"<div style='background:#f0f2f6;padding:15px;border-radius:10px'>{suggestions}</div>",
                unsafe_allow_html=True
            )
