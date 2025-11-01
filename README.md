🧠 AI Supervisor System

A self-learning AI system built using FastAPI, MongoDB, and JavaScript.
It allows supervisors to teach the AI new answers, and once learned, the AI automatically responds correctly in future conversations.

---

🚀 Overview

The AI Supervisor System is designed to demonstrate a simple human-in-the-loop AI learning workflow:

* The AI answers questions it already knows.
* If it doesn’t know, it asks a human supervisor.
* Once the supervisor provides an answer, the AI learns permanently.

This project uses FastAPI for the backend, MongoDB for storing data, and HTML/CSS/JS for the frontend interface.

---

🧩 Features

* Ask AI questions directly from the dashboard
* AI answers immediately if it knows the answer
* Supervisor can see all unanswered questions
* Supervisor adds answers → AI learns automatically
* Clean, modern dashboard design
* Fully connected with MongoDB for persistent learning

---

🏗️ Project Structure

```
AI-Supervisor-System/
│
├── backend/
│   ├── main.py          # FastAPI backend and routes
│   ├── ai_agent.py      # AI logic (response + learning)
│   ├── database.py      # MongoDB connection
│   ├── models.py        # Pydantic models for clean data handling
│
├── frontend/
│   ├── index.html       # Frontend UI dashboard
│   ├── styles.css       # Modern gradient glassmorphism CSS
│
├── venv/                # Python virtual environment (not uploaded)
├── .gitignore           # Excludes venv and cache files
├── requirements.txt     # Python package dependencies
└── README.md            # Project documentation
```

---

⚙️ Step-by-Step Setup Guide

1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Supervisor-System.git
cd AI-Supervisor-System
```

---

2️⃣ Create a Virtual Environment

Create a Python virtual environment to keep dependencies isolated.

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

3️⃣ Install Required Packages

Once your environment is activated, install all dependencies:

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt` yet, run this to create it:

```bash
pip freeze > requirements.txt
```

---

4️⃣ Set Up MongoDB

Option 1: Local MongoDB Compass

1. Install MongoDB and MongoDB Compass.
2. Open Compass and connect using:

   ```
   mongodb://localhost:27017
   ```
3. Create a database named `ai_supervisor`.
4. Collections will be created automatically:

   * help_requests
   * knowledge_base

Option 2: MongoDB Atlas (Cloud)

* Go to [https://www.mongodb.com/atlas](https://www.mongodb.com/atlas)
* Create a free cluster
* Replace your connection string in `backend/database.py`

---

5️⃣ Run the FastAPI Server

```bash
uvicorn backend.main:app --reload
```

Output:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

---

6️⃣ Open the Dashboard

Open your browser and go to:

```
http://127.0.0.1:8000/frontend
```

You’ll see your AI Supervisor Dashboard — start chatting and teaching your AI!

---

🧠 How It Works

1. You ask a question from the dashboard.
2. FastAPI checks MongoDB for a matching question.
3. If found → AI replies immediately.
4. If not → the question goes to help_requests.
5. Supervisor reviews unanswered questions.
6. Supervisor provides an answer.
7. Answer is stored in knowledge_base.
8. Next time, AI answers automatically!

---

🧰 Technologies Used

| Category   | Technology                               |
| ---------- | ---------------------------------------- |
| Backend    | FastAPI, Python                          |
| Database   | MongoDB, PyMongo                         |
| Frontend   | HTML, CSS, JavaScript                    |
| Server     | Uvicorn                                  |
| Validation | Pydantic Models                          |
| Styling    | Gradient + Glassmorphism                 |
| Tools      | VS Code, MongoDB Compass, GitHub Desktop |

---

🧾 requirements.txt Example

```
fastapi==0.120.4
uvicorn==0.30.6
pymongo==4.15.3
pydantic==2.12.3
dnspython==2.8.0
```

---

💡 Common Commands

| Task                 | Command                           |
| -------------------- | --------------------------------- |
| Create environment   | python -m venv venv               |
| Activate (Windows)   | venv\Scripts\activate             |
| Activate (Mac/Linux) | source venv/bin/activate          |
| Install packages     | pip install -r requirements.txt   |
| Run server           | uvicorn backend.main:app --reload |
| Update dependencies  | pip freeze > requirements.txt     |

---

🎨 Design Notes

* Modern gradient + glassmorphism UI
* Smooth hover and fade animations
* Fully responsive
* Clear separation between AI and supervisor roles

---

🚀 Future Improvements

* Add login authentication for supervisors
* Improve AI with fuzzy/semantic matching
* Add chat or voice interface
* Deploy on Render or Heroku with MongoDB Atlas

---

👨‍💻 Author

Aamir Khan
Developed as a part of an AI learning and automation project.
📧 aamir.khan471712@gmail.com(mailto:aamir.khan471712@gmail.com)

---

🏁 Summary

This project shows how human intelligence and machine learning can work together.
It’s simple yet powerful — an AI that keeps getting smarter with every interaction.
