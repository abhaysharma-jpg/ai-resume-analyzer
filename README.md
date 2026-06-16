# AI Resume Analyzer 🤖

An AI-powered tool that analyzes your resume against a job description.

## Features
- ATS match score
- Skills gap analysis
- Keyword matching
- Actionable improvement tips

## Tech Stack
- **Backend**: Python + Flask
- **AI**: Groq LLaMA API (llama-3.3-70b-versatile)
- **PDF Parsing**: PyMuPDF
- **Frontend**: HTML + CSS + Vanilla JS

## Setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

## create .env file
GROQ_API_KEY=your-api-key

## Run
python app.py
Open http://localhost:5000