"""
Input Validation Utility
"""


def validate_inputs(resume_text: str, job_description: str) -> str | None:
    """
    Validate resume text and job description.
    Returns error string if invalid, None if valid.
    """
    if not resume_text:
        return "Resume text is required. Please upload a PDF or paste your resume."

    if not job_description:
        return "Job description is required."

    if len(resume_text) < 100:
        return "Resume seems too short. Please provide more content."

    if len(job_description) < 50:
        return "Job description seems too short. Please provide more details."

    if len(resume_text) > 15000:
        return "Resume text is too long (max 15,000 characters)."

    if len(job_description) > 10000:
        return "Job description is too long (max 10,000 characters)."

    return None
