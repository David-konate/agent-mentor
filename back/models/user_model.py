# -*- coding: utf-8 -*-
"""
user_model.py  (couche MODEL)
=============================
Accès aux données de la table `users` (le SQL, rien d'autre).
Requêtes PARAMÉTRÉES (%s) pour éviter les injections SQL.
"""
from database import get_connection


def create_user(first_name, email, password_hash):
    """Insère un nouvel utilisateur et renvoie son id."""
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO users (first_name, email, password_hash) VALUES (%s, %s, %s)",
            (first_name, email, password_hash),
        )
        new_id = cur.lastrowid
    conn.close()
    return new_id


def find_by_email(email):
    """Renvoie l'utilisateur ayant cet email (un dict), ou None."""
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
    conn.close()
    return user
