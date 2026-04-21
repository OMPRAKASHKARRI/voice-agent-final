# 🎤 Voice AI Appointment Booking System

An AI-powered, real-time voice assistant that enables users to book medical appointments using natural language (voice or text).

---

## 📌 Overview

Traditional appointment booking systems are manual, time-consuming, and prone to errors.  
This project introduces an **intelligent conversational agent** that understands user intent and automates the entire booking process.

---

## ✨ Key Features

- 🎤 Voice Input (Browser Speech Recognition)
- 🔊 Voice Output (Speech Synthesis)
- 💬 Real-time Communication using WebSockets
- 🤖 AI Intent Understanding (Groq LLM)
- 🧠 Session Memory (Redis)
- 🗄️ PostgreSQL Database Integration
- ⚠️ Conflict Detection (prevents double booking)
- 🌐 Multilingual Support (basic)

---

## 🏗️ System Architecture
User (Voice/Text)
↓
Speech Recognition (Browser)
↓
WebSocket (FastAPI Backend)
↓
AI Agent (Groq LLM)
↓
Scheduler Engine + PostgreSQL
↓
Response → UI + Voice Output

---

## 🛠️ Tech Stack

| Layer        | Technology                     |
|-------------|------------------------------|
| Frontend     | HTML, CSS, JavaScript         |
| Backend      | FastAPI (Python)              |
| AI Model     | Groq LLM                      |
| Database     | PostgreSQL                    |
| Cache        | Redis                         |
| Communication| WebSockets                    |
| Voice Input  | Web Speech API                |
| Voice Output | Speech Synthesis API          |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/voice-agent-final.git
cd voice-agent-final
```
### 2. Setup Backend
cd backend
pip install -r requirements.txt

### 3. Configure Environment Variables
Create a .env file inside the backend/ folder:

GROQ_API_KEY=your_api_key
DB_HOST=localhost
DB_NAME=appointments
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432


### 4. Run Backend Server
python -m uvicorn backend.main:app --reload
Server will start at:
http://127.0.0.1:8000

### 5. Run Frontend
Open the index.html file in your browser
(or use VS Code Live Server)

🎯 Usage


Click the 🎙 microphone button


Speak naturally:


Book appointment tomorrow


Continue conversation:


Cardiologist10:00


Appointment gets booked successfully ✅



🔄 Example Conversation
User: Book appointment tomorrow
AI: Which doctor would you like?
User: CardiologistAI: Available slots: 10:00, 
14:00User: 10:00
AI: Appointment booked successfully

⚠️ Important Notes


Do NOT push .env file to GitHub ❌


Use wss:// instead of ws:// in production


Voice features require HTTPS in deployment



- 🚀 Future Enhancements


- 📱 Mobile Application


- 🌍 Advanced Multilingual Support


- 📊 Admin Dashboard


- 📅 Google Calendar Integration


- 🔐 Authentication System



### 👨‍💻 Author
Om Prakash Karri


