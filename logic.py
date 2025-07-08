import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompts import build_tech_prompt

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_questions(name, tech_stack):
    prompt = build_tech_prompt(name, tech_stack)
    try:
        chat = model.start_chat()
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error generating questions: {e}"
