# -*- coding: utf-8 -*-
"""
app.py
======
Le BACK (serveur) en Python avec Flask.

Responsabilites :
  1. Servir le front (HTML/CSS/JS) du dossier "front/".
  2. Exposer une route /api/chat qui recoit la question du junior,
     applique la convention pedagogique (prompt.py) et interroge Gemini.

La cle API reste cote serveur : le front ne la voit jamais.
"""

import os
from flask import Flask, request, jsonify, send_from_directory

# Charge le fichier .env en local (sur o2switch, les variables sont definies
# dans cPanel, et load_dotenv ne fait rien de genant s'il n'y a pas de .env).
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from prompt import construire_system_prompt
from gemini_client import demander_a_gemini

# Dossier contenant le front (index.html, style.css, app.js).
DOSSIER_FRONT = os.path.join(os.path.dirname(__file__), "front")

app = Flask(__name__, static_folder=DOSSIER_FRONT, static_url_path="")


@app.route("/")
def accueil():
    """Sert la page de chat."""
    return send_from_directory(DOSSIER_FRONT, "index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    """
    Recoit la conversation, interroge l'agent, renvoie sa reponse.

    Corps attendu (JSON) :
    {
      "mode": "tuteur" | "copilote",
      "messages": [
        {"role": "user", "content": "..."},
        {"role": "assistant", "content": "..."}
      ]
    }
    """
    donnees = request.get_json(silent=True) or {}
    mode = donnees.get("mode", "tuteur")
    messages = donnees.get("messages", [])

    if not messages:
        return jsonify({"erreur": "Aucun message fourni."}), 400

    # On construit le system prompt selon le mode pedagogique (Article 4).
    system_prompt = construire_system_prompt(mode)

    try:
        reponse = demander_a_gemini(system_prompt, messages)
    except Exception as exc:  # noqa: BLE001 (on veut un message propre cote front)
        return jsonify({"erreur": f"Erreur cote serveur : {exc}"}), 500

    return jsonify({"reponse": reponse})


if __name__ == "__main__":
    # Lancement en LOCAL uniquement (pour developper sur ta machine).
    # Sur o2switch, c'est Passenger qui lance l'app via passenger_wsgi.py.
    app.run(host="127.0.0.1", port=5000, debug=True)
