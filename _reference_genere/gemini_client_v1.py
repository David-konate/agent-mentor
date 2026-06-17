import os          # pour lire les variables d'environnement
import requests    # pour envoyer des requêtes HTTP (la lib qu'on a installée)


def demander_a_gemini(system_prompt, messages):
    # 1. Récupérer la clé API depuis l'environnement (jamais en dur dans le code !)
    cle_api = os.environ.get("GEMINI_API_KEY")
    if not cle_api:
        raise RuntimeError("La clé API Gemini est absente. Vérifie ton fichier .env.")

    # 2. Traduire les messages au format attendu par Gemini
    contents = []
    for message in messages:
        if message["role"] == "assistant":
            role = "model"
        else:
            role = "user"
        contents.append({
            "role": role,
            "parts": [{"text": message["content"]}],
        })

    # 3. Assembler le corps de la requête (le "colis" envoyé à Gemini)
    corps = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": contents,
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 1024,
        },
    }

    # 4. Envoyer le colis à Gemini
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    reponse = requests.post(url, params={"key": cle_api}, json=corps, timeout=30)
    reponse.raise_for_status()
    donnees = reponse.json()

    # 5. Extraire le texte de la réponse
    try:
        return donnees["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        return "Je n'ai pas pu générer de réponse. Essaie de reformuler ta question."
