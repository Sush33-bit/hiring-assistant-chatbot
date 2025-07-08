def build_tech_prompt(name, tech_stack):
    return f"""
You are a hiring assistant for TalentScout.
A candidate named {name} has skills in the following tech stack: {tech_stack}.
Ask 3–5 technical interview questions to evaluate their proficiency.
"""

def greeting_message():
    return "👋 Hello! I'm your AI Hiring Assistant. Let's begin the screening process."

def farewell_message():
    return "✅ Thank you! We've recorded your information. Our team will get back to you."

def fallback_message():
    return "❓ Sorry, I didn’t get that. Please clarify your input."
