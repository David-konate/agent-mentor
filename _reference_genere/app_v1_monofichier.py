import os
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv

load_dotenv()  # charge la clé Groq depuis le .env

import prompt          # ton cerveau (construire_prompt)
import groq_client     # ton client IA (demander_a_groq)

# Crée l'application web. static_folder="front" dit à Flask où sont
# les fichiers du front (qu'on créera juste après).
app = Flask(__name__, static_folder="front", static_url_path="")


@app.route("/")
def accueil():
    # Sert la page de chat (front/index.html) quand on visite la racine du site.
    return send_from_directory("front", "index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    # 1. Lire ce que le front envoie (le mode + la conversation)
    donnees = request.get_json()
    mode = donnees.get("mode", "tuteur")
    messages = donnees.get("messages", [])

    # 2. Construire le system prompt selon le mode (on réutilise prompt.py !)
    system = prompt.construire_prompt(mode)

    # 3. Demander la réponse à l'IA (on réutilise groq_client.py !)
    reponse = groq_client.demander_a_groq(system, messages)

    # 4. Renvoyer la réponse au front, au format JSON
    return jsonify({"reponse": reponse})

if __name__ == "__main__":
    # Lancement en local (sur ta machine) pour développer.
    # Sur o2switch, c'est Passenger qui démarre l'app, pas cette ligne.
    app.run(host="127.0.0.1", port=5000, debug=True)