# backend/ai_agent.py
from backend.database import knowledge_base
import re

# -------------------------------------
# Clean text (remove punctuation, make lowercase)
# -------------------------------------
def clean_text(text: str):
    """Normalize text for consistent matching."""
    return re.sub(r'[^\w\s]', '', text.lower().strip())

# -------------------------------------
# AI Response Function
# -------------------------------------
def ai_response(question):
    cleaned_question = clean_text(question)

    # 1️⃣ Check MongoDB (knowledge_base)
    existing = knowledge_base.find_one({"question": cleaned_question})
    if existing:
        return existing["answer"]

    # 2️⃣ Check some built-in defaults (optional)
    known_answers = {
        "what are your timings": "We are open from 9 AM to 6 PM.",
        "where are you located": "We are located in Bangalore",
        "How much you charge for facial": "200 rupees"
    }
    if cleaned_question in known_answers:
        return known_answers[cleaned_question]

    # 3️⃣ Otherwise, escalate to supervisor
    return "HELP_REQUEST"
