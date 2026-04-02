import google.generativeai as genai
import json

genai.configure(api_key="AIzaSyCqyo4N2wa5_xHquv8oCzv1U60kYO-nT1M")

model = genai.GenerativeModel("models/gemini-2.5-flash")

def analyze_updates(updates):
    text_data = "\n".join([
        f"{u.competitor.name}: {u.title}"
        for u in updates
    ])

    prompt = f"""
    You are a product strategist.

    Analyze competitor signals and return STRICT JSON:

    {{
      "features": [],
      "messaging_trends": [],
      "customer_pain_points": [],
      "weaknesses": []
    }}

    Data:
    {text_data}
    """

    try:
        response = model.generate_content(prompt)
        return clean_json(response.text)
    except Exception as e:
        return f"Error: {str(e)}"


def generate_recommendations(insights):
    prompt = f"""
        Return GTM strategy ALWAYS as array with at least 3 items.

    [
      {{
        "phase": "Phase name",
        "goal": "Goal",
        "tactics": ["tactic1", "tactic2"]
      }}
    ]
    """

    try:
        response = model.generate_content(prompt)
        return clean_json(response.text)
    except Exception as e:
        return f"Error: {str(e)}"



def clean_json(text):
    try:
        text = text.strip()

        # remove ```json and ```
        if text.startswith("```"):
            text = text.replace("```json", "").replace("```", "")

        return json.loads(text)

    except Exception:
        return {"error": "Invalid JSON", "raw": text}