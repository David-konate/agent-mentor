import os
import requests


def ask_groq(system_prompt, messages):
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("La clé API Groq est absente. Vérifie ton fichier .env.")

    # format openai : le system prompt en 1er message
    groq_messages = [{"role": "system", "content": system_prompt}]
    for message in messages:
        groq_messages.append({"role": message["role"], "content": message["content"]})

    body = {
        "model": os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile"),
        "messages": groq_messages,
        "temperature": 0.7,
        "max_tokens": 1024,
    }

    # auth par header Bearer
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": "Bearer " + api_key}
    response = requests.post(url, headers=headers, json=body, timeout=30)
    response.raise_for_status()
    data = response.json()

    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError):
        return "Je n'ai pas pu générer de réponse. Essaie de reformuler ta question."
