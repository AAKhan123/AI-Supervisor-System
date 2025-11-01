from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ai_supervisor_db"]  
help_requests = db["help_requests"] 
knowledge_base = db["knowledge_base"]
