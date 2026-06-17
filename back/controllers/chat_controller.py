# -*- coding: utf-8 -*-
"""
chat_controller.py  (couche CONTROLLER)
=======================================
La LOGIQUE métier d'un échange de chat : construit le prompt, interroge l'IA.
"""
from services.prompt import build_prompt
from services.groq_client import ask_groq
from models.message_model import save_message, get_messages


def handle_chat(user_id, first_name, mode, messages):          # ← + first_name
    """Construit le prompt, interroge l'IA, puis sauvegarde l'échange."""
    system_prompt = build_prompt(mode, first_name)             # ← + first_name
    response = ask_groq(system_prompt, messages)

    if messages:
        save_message(user_id, "user", messages[-1]["content"])
    save_message(user_id, "assistant", response)

    return response


def get_history(user_id):
    """Renvoie l'historique des messages d'un utilisateur."""
    return get_messages(user_id)