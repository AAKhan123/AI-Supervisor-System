
from backend.database import knowledge_base
import re


def clean_text(text: str):
    """Normalize text for consistent matching."""
    return re.sub(r'[^\w\s]', '', text.lower().strip())


def ai_response(question):
    cleaned_question = clean_text(question)

    existing = knowledge_base.find_one({"question": cleaned_question})
    if existing:
        return existing["answer"]


    known_answers = {
        "what are your timings": "We are open from 9 AM to 6 PM.",
        "where are you located": "We are located in Bangalore",
        "How much you charge for facial": "200 rupees"
    }
    if cleaned_question in known_answers:
        return known_answers[cleaned_question]


    return "HELP_REQUEST"
