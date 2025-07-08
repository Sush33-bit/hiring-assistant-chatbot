# 🤖 AI Hiring Assistant Chatbot

This is an AI-powered Hiring Assistant chatbot built for TalentScout that screens candidates based on their tech stack and generates custom technical interview questions using Gemini (`gemini-1.5-flash`).

---

## 🚀 Features

- Collects candidate details (Name, Email, Phone, Experience, Tech Stack)
- Uses **Google Gemini (`gemini-1.5-flash`)** to generate 3–5 tailored technical questions
- Clean and simple **Streamlit UI**
- Graceful greeting, fallback, and conversation end
- Modular code using Python files: `app.py`, `logic.py`, `prompts.py`
- Secure `.env` key handling using `python-dotenv`

---

## 🛠 Tech Stack

- Python
- Streamlit
- Google Gemini (`gemini-1.5-flash`)
- `google-generativeai` SDK
- `python-dotenv` for secure key handling

---

## ⚙️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/Sush33-bit/hiring-assistant-chatbot.git
cd hiring-assistant-chatbot
