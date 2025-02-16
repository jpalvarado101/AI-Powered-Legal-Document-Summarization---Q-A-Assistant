import re

def clean_text(text: str) -> str:
    # Remove extra spaces and newlines, then trim the text.
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
