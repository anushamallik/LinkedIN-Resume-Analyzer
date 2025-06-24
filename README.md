# LinkedIN-Resume-Analyzer
Semantic matching engine that evaluates resumes against job descriptions using NLP, BERT embeddings, and cosine similarity — with improvement suggestions via a smart interface.

## FEATURES

- Compare your resume with any job description
- Semantic similarity using BERT embeddings
- Highlighted improvement suggestions
- User-friendly Streamlit interface with optional dark mode

---

## TECH-STACK

- **Frontend**: Streamlit
- **Backend**: Python
- **NLP Models**: Sentence Transformers (BERT), Scikit-learn
- **Libraries**: PDFPlumber, Transformers, Torch, Pandas

---
## Project Structure

linkedin_resume_analyzer/
├── app.py # Streamlit frontend
├── requirements.txt
└── backend/
├── resume_parser.py # Extracts text from resume PDFs
├── job_parser.py # Processes job descriptions
├── match_engine.py # Computes similarity scores
├── suggestions.py # Suggests improvements
└── utils.py # Text cleaning and helpers


#  Clone the repository
git clone https://github.com/anushamallik/linkedin-resume-analyzer.git
cd linkedin-resume-analyzer
# Create virtual environment
python -m venv venv
# Activate the environment (PowerShell)
.\venv\Scripts\Activate.ps1
# Install dependencies
pip install -r requirements.txt
# Run
streamlit run app.py

# HOW IT WORKS?
1.Upload Resume (PDF) — Extracts content using pdfplumber
2.Paste Job Description — Text area input
3.Semantic Embedding — BERT-based sentence transformer converts texts into vectors
4.Similarity Score — Cosine similarity shows how well your resume matches the job
5.Suggestions — Key missing areas are listed for improvement



