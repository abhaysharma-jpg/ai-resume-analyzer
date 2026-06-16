# AI Resume Analyzer 🤖

An AI-powered tool that analyzes your resume against a job description and gives you:
- ATS match score
- Skills gap analysis
- Keyword matching
- Actionable improvement tips

## Tech Stack
## Tech Stack
- **Backend**: Python + Flask
- **AI**: Groq LLaMA API (llama-3.3-70b-versatile)
- **PDF Parsing**: PyMuPDF
- **Frontend**: HTML + CSS + Vanilla JS
- **Deployment**: Docker + Google Cloud Run

## Project Structure
```
resume_analyzer/
├── app.py                  # Main Flask app
├── utils/
│   ├── ai_analyzer.py      # API integration
│   ├── pdf_extractor.py    # PDF text extraction
│   └── validator.py        # Input validation
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   ├── css/style.css       # Styles
│   └── js/main.js          # Frontend logic
├── requirements.txt
├── Dockerfile
└── .env.example
```

## Setup & Run Locally

### 1. Clone & install dependencies
```bash
git clone <your-repo-url>
cd resume_analyzer
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set your API key
```bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### 3. Run the app
```bash
python app.py
```
Open http://localhost:5000

## Deploy to Google Cloud Run
```bash
# Build Docker image
docker build -t resume-analyzer .

# Tag for GCR
docker tag resume-analyzer gcr.io/YOUR_PROJECT_ID/resume-analyzer

# Push
docker push gcr.io/YOUR_PROJECT_ID/resume-analyzer

# Deploy
gcloud run deploy resume-analyzer \
  --image gcr.io/YOUR_PROJECT_ID/resume-analyzer \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars ANTHROPIC_API_KEY=your_key_here
```

## API Endpoints
- `GET /` — Main UI
- `POST /analyze` — Analyze resume (form-data: resume_file or resume_text + job_description)
- `GET /health` — Health check

## Resume (for your portfolio)
> Built a full-stack AI Resume Analyzer using Python (Flask), Anthropic Claude API, and PyMuPDF. Deployed on Google Cloud Run via Docker. Features PDF parsing, ATS scoring, keyword gap analysis, and real-time AI feedback.
