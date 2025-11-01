from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from datetime import datetime
from bson import ObjectId
import os

from backend.database import help_requests, knowledge_base
from backend.ai_agent import ai_response, clean_text

app = FastAPI(title="AI Supervisor System", version="1.0.0")

# -------------------------------------------------------
# ✅ Enable CORS (so frontend can communicate with backend)
# -------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------------------------------------
# ✅ Helper: convert Mongo ObjectId to string
# -------------------------------------------------------
def serialize(doc):
    doc["_id"] = str(doc["_id"])
    return doc


# -------------------------------------------------------
# ✅ Health check route
# -------------------------------------------------------
@app.get("/")
def home():
    return {"message": "AI Supervisor System is running"}


# -------------------------------------------------------
# ✅ Ask AI endpoint
# -------------------------------------------------------
@app.post("/ask-ai/")
def ask_ai(question: str):
    response = ai_response(question)

    if response == "HELP_REQUEST":
        help_requests.insert_one({
            "question": question,
            "status": "pending",
            "answer": None,
            "created_at": datetime.now()
        })
        return {"message": "Let me check with my supervisor and get back to you."}

    return {"answer": response}


# -------------------------------------------------------
# ✅ Supervisor: View all requests
# -------------------------------------------------------
@app.get("/requests/")
def get_requests():
    data = [serialize(req) for req in help_requests.find()]
    return data


# -------------------------------------------------------
# ✅ Supervisor: Answer a pending request
# -------------------------------------------------------
@app.post("/requests/{req_id}/answer/")
def answer_request(req_id: str, answer: str):
    # Update request status
    help_requests.update_one(
        {"_id": ObjectId(req_id)},
        {"$set": {"answer": answer, "status": "resolved"}}
    )

    # Get the resolved request
    req = help_requests.find_one({"_id": ObjectId(req_id)})

    # ✅ Store the cleaned question in knowledge base for AI learning
    cleaned_q = clean_text(req["question"])
    knowledge_base.insert_one({
        "question": cleaned_q,
        "answer": answer
    })

    return {"message": f"AI learned: {req['question']} -> {answer}"}


# -------------------------------------------------------
# ✅ Supervisor: View knowledge base
# -------------------------------------------------------
@app.get("/knowledge-base/")
def get_knowledge():
    data = [serialize(kb) for kb in knowledge_base.find()]
    return data


# -------------------------------------------------------
# ✅ Serve Frontend (Dashboard)
# -------------------------------------------------------
@app.get("/frontend")
def serve_frontend():
    frontend_path = os.path.join(os.path.dirname(__file__), "../frontend/index.html")
    return FileResponse(frontend_path)
