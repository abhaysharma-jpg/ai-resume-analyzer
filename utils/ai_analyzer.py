from groq import Groq
import json
import re
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are an expert ATS (Applicant Tracking System) analyst and senior career coach with 15+ years of experience in talent acquisition.

Return ONLY a valid JSON object — no markdown, no explanation, no extra text.

JSON structure:
{
  "overall_score": <integer 0-100>,
  "skills_score": <integer 0-100>,
  "experience_score": <integer 0-100>,
  "keyword_score": <integer 0-100>,
  "ats_score": <integer 0-100>,
  "matched_keywords": [<up to 15 keywords/skills present in BOTH resume and JD>],
  "missing_keywords": [<up to 12 important skills/keywords from JD missing in resume>],
  "strengths": [<4-6 specific strengths of this resume for this exact role>],
  "suggestions": [<5-7 specific, actionable improvements to better match this JD>],
  "summary": "<2-3 sentence overall assessment>",
  "experience_level_match": "<one of: Strong Match, Partial Match, Weak Match>",
  "top_missing_skill": "<the single most critical missing skill>"
}"""


def analyze_resume(resume_text: str, job_description: str) -> dict:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"RESUME:\n{resume_text}\n\n---\n\nJOB DESCRIPTION:\n{job_description}\n\n---\n\nAnalyze and return ONLY the JSON object."}
        ],
        temperature=0.3,
        max_tokens=1500
    )
    raw = response.choices[0].message.content.strip()
    raw = re.sub(r'^```(?:json)?\s*', '', raw)
    raw = re.sub(r'\s*```$', '', raw)
    return json.loads(raw)