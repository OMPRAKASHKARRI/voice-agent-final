import os
import json
import re
from dotenv import load_dotenv
from pathlib import Path
from groq import Groq

# ✅ IMPORTS (THIS FIXES YOUR ERROR)
from backend.agent.tools import handle_tools
from backend.memory.session import get_session, update_session

# 🔥 ENV LOAD
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print("GROQ KEY DEBUG:", GROQ_API_KEY)

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found")

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
You are a medical appointment assistant.

Return ONLY valid JSON. No explanation.

Format:
{
  "intent": "book | cancel | reschedule",
  "doctor": null,
  "date": null,
  "time": null
}

Rules:
- Extract only what user says
- Missing fields must be null
- NEVER return text outside JSON
"""


# ✅ Robust JSON extractor
def extract_json(text: str):
    text = re.sub(r"```json|```", "", text).strip()

    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None

    try:
        return json.loads(match.group(0))
    except Exception as e:
        print("JSON PARSE ERROR:", e)
        return None


# ✅ LLM call
def run_agent(user_input: str):
    try:
        resp = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ]
        )

        content = resp.choices[0].message.content.strip()
        print("LLM RAW:", content)

        data = extract_json(content)

        # 🛑 fallback if parsing fails
        if not data:
            print("⚠️ JSON parse failed — using fallback")
            return {
                "intent": "book",
                "doctor": None,
                "date": None,
                "time": None
            }

        # 🧠 normalize keys (safety)
        return {
            "intent": data.get("intent"),
            "doctor": data.get("doctor"),
            "date": data.get("date"),
            "time": data.get("time")
        }

    except Exception as e:
        print("LLM ERROR:", e)

        return {
            "intent": "book",
            "doctor": None,
            "date": None,
            "time": None
        }


# ✅ Main orchestrator
def process_request(user_input, session_id):
    session = get_session(session_id)

    data = run_agent(user_input)
    print("TOOL INPUT:", data)

    response = handle_tools(data, session)

    update_session(session_id, session)

    return response