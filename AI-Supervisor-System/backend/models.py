# backend/models.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ----------------------------
# Model for Help Requests
# ----------------------------
class HelpRequest(BaseModel):
    id: Optional[str] = None
    question: str
    answer: Optional[str] = None
    status: str = "pending"   # default status
    created_at: datetime = datetime.utcnow()

# ----------------------------
# Model for Knowledge Base
# ----------------------------
class KnowledgeItem(BaseModel):
    id: Optional[str] = None
    question: str
    answer: str
    created_at: datetime = datetime.utcnow()
