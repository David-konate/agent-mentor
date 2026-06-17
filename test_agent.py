# test_agent.py
# Petit script pour tester l'agent SANS lancer tout le serveur.
# Lancer avec :  ./venv/Scripts/python.exe test_agent.py

import sys
import os

# On ajoute back/ au chemin pour pouvoir importer les couches.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "back"))

import config  # charge le .env (clé Groq)
from services.prompt import build_prompt
from services.groq_client import ask_groq

# On construit le system prompt en mode tuteur
system_prompt = build_prompt("tutor")

# On simule une demande PASSIVE d'un junior (l'agent devrait refuser + guider)
messages = [
    {"role": "user", "content": "Écris à ma place une fonction Python qui calcule la factorielle d'un nombre."}
]

print("=== Question du junior (demande passive) ===")
print(messages[0]["content"])
print()
print("=== Réponse de ton agent Mentor Senior ===")
print(ask_groq(system_prompt, messages))
