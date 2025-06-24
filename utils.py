
# backend/utils.py

import re

def clean_text(text):
    """
    Clean and normalize input text:
    - Converts to lowercase
    - Removes extra whitespace
    - Strips special characters (optional)
    """
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)  # Replace multiple whitespace with single space
    return text
