"""
PDF Text Extraction Utility
Uses PyMuPDF (fitz) for fast, accurate PDF parsing
"""

import fitz  # PyMuPDF
import os


def extract_text_from_pdf(filepath: str) -> str:
    """
    Extract all text from a PDF file.
    Returns cleaned plain text string.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"PDF not found: {filepath}")

    text_parts = []

    with fitz.open(filepath) as doc:
        for page_num, page in enumerate(doc):
            page_text = page.get_text("text")
            if page_text.strip():
                text_parts.append(page_text)

    full_text = "\n".join(text_parts)
    return clean_text(full_text)


def clean_text(text: str) -> str:
    """Remove excessive whitespace and normalize text."""
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        line = line.strip()
        if line:
            cleaned.append(line)
    return "\n".join(cleaned)
