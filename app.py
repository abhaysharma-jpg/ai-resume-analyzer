"""
AI-Powered Resume Analyzer
Main Flask Application
"""
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from utils.pdf_extractor import extract_text_from_pdf
from utils.ai_analyzer import analyze_resume
from utils.validator import validate_inputs
import uuid

app = Flask(__name__)
CORS(app)

app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'txt'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        resume_text = ''
        job_description = request.form.get('job_description', '').strip()

        if 'resume_file' in request.files:
            file = request.files['resume_file']
            if file and file.filename and allowed_file(file.filename):
                filename = f"{uuid.uuid4().hex}.pdf"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                resume_text = extract_text_from_pdf(filepath)
                os.remove(filepath)

        if not resume_text:
            resume_text = request.form.get('resume_text', '').strip()

        error = validate_inputs(resume_text, job_description)
        if error:
            return jsonify({'success': False, 'error': error}), 400

        result = analyze_resume(resume_text, job_description)
        return jsonify({'success': True, 'data': result})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'version': '1.0.0'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
