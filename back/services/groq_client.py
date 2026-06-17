import os
import requests


def _detect_lang(texte):
   
    t = " " + texte.lower() + " "
    if any(c in t for c in "éèêàâçùîôœ"):   # accents = francais quasi sur
        return "fr"
    mots_fr = [" le ", " la ", " les ", " un ", " une ", " des ", " est ", " c'est", " quoi",
               " comment", " pourquoi", " je ", " tu ", " ça ", " dans ", " pour ", " avec ",
               " que ", " qu'", " ne ", " pas ", " quel", " mon ", " ma ", " mes "]
    mots_en = [" the ", " is ", " a ", " an ", " what", " how", " why", " you ", " i ", " of ",
               " to ", " and ", " in ", " for ", " with ", " do ", " does", " can ", " explain",
               " my ", " this ", " that ", " are "]
    fr = sum(t.count(m) for m in mots_fr)
    en = sum(t.count(m) for m in mots_en)
    return "en" if en > fr else "fr"   

def ask_groq(system_prompt, messages):
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("La clé API Groq est absente. Vérifie ton fichier .env.")

    # format openai : le system prompt en 1er message
    groq_messages = [{"role": "system", "content": system_prompt}]
    for message in messages:
        groq_messages.append({"role": message["role"], "content": message["content"]})

    # on detecte la langue de la question et on FORCE la reponse dans cette langue
    if groq_messages and groq_messages[-1]["role"] == "user":
        lang = _detect_lang(messages[-1]["content"])
        rappel = " (Reply ENTIRELY in English.)" if lang == "en" else " (Réponds ENTIÈREMENT en français.)"
        groq_messages[-1] = {"role": "user", "content": groq_messages[-1]["content"] + rappel}

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
