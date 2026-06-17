import os          # pour lire les variables d'environnement
import requests    # pour envoyer des requêtes HTTP


def ask_groq(system_prompt, messages):
    # 1. Récupérer la clé API depuis l'environnement (jamais en dur dans le code !)
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("La clé API Groq est absente. Vérifie ton fichier .env.")

    # 2. Construire la liste des messages au format Groq (compatible OpenAI)
    #    -> Le system prompt devient un message de rôle "system", placé en tête.
    groq_messages = [{"role": "system", "content": system_prompt}]
    for message in messages:
        groq_messages.append({
            "role": message["role"],       # "user" ou "assistant"
            "content": message["content"],
        })

    # 3. Assembler le corps de la requête (le "colis")
    body = {
        "model": os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile"),
        "messages": groq_messages,
        "temperature": 0.7,
        "max_tokens": 1024,
    }

    # 4. Envoyer le colis à Groq (authentification par en-tête Authorization: Bearer)
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": "Bearer " + api_key}
    response = requests.post(url, headers=headers, json=body, timeout=30)
    response.raise_for_status()
    data = response.json()

    # 5. Extraire le texte de la réponse (format OpenAI : choices[0].message.content)
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError):
        return "Je n'ai pas pu générer de réponse. Essaie de reformuler ta question."
