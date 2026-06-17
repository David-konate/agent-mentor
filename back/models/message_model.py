# -*- coding: utf-8 -*-
"""
message_model.py  (couche MODEL)
================================
Accès aux données de la table `messages` (le SQL, rien d'autre).
Requêtes PARAMÉTRÉES (%s) anti-injection.
"""
from database import get_connection


def save_message(user_id, role, content):
    """Enregistre un message lié à un utilisateur."""
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(
            # à toi : INSERT dans messages (user_id, role, content)
           "INSERT INTO messages (user_id, role, content) VALUES (%s, %s, %s)",
            (user_id, role, content),
        )
    conn.close()


def get_messages(user_id):
    """Renvoie tous les messages d'un utilisateur, du plus ancien au plus récent."""
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(
            # à toi : SELECT role, content WHERE user_id = %s ORDER BY created_at
            "SELECT role, content FROM messages WHERE user_id = %s ORDER BY created_at",
            (user_id,),
        )
        messages = cur.fetchall()
    conn.close()
    return messages
