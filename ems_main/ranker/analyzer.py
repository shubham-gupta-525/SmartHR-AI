import re
import pdfplumber
import spacy
from docx import Document

nlp = spacy.load("en_core_web_sm")

IMPORTANT_SKILLS = [
    "python", "django", "rest", "api", "sql", "flask",
    "pandas", "numpy", "git", "linux"
]


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()


def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + " "
    return text.lower()


def extract_text(file_path):
    """
    Auto-detect file type and extract text
    """
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        return ""


def extract_experience(text):
    matches = re.findall(r'(\d+)\+?\s*(years|yrs)', text)
    if matches:
        return max(int(m[0]) for m in matches)
    return 0


def calculate_score(job_desc, resume_text):
    score = 0

    # ---------- 1. SKILLS (50 points) ----------
    skill_hits = sum(1 for skill in IMPORTANT_SKILLS if skill in resume_text)
    score += min((skill_hits / len(IMPORTANT_SKILLS)) * 50, 50)

    # ---------- 2. EXPERIENCE (30 points) ----------
    years = extract_experience(resume_text)
    if years >= 8:
        score += 30
    elif years >= 5:
        score += 22
    elif years >= 3:
        score += 15
    elif years >= 1:
        score += 8

    # ---------- 3. ROLE MATCH (10 points) ----------
    if "python developer" in resume_text:
        score += 10

    # ---------- 4. JOB DESCRIPTION KEYWORDS (10 points) ----------
    job_doc = nlp(job_desc.lower())
    keywords = [t.text for t in job_doc if t.is_alpha and not t.is_stop]
    hits = sum(1 for w in keywords if w in resume_text)

    if keywords:
        score += min((hits / len(keywords)) * 10, 10)

    return round(min(score, 100), 2)
