# -*- coding: utf-8 -*-
"""
auth_controller.py  (couche CONTROLLER)
=======================================
La LOGIQUE d'authentification : inscription (hash + création) et
connexion (vérification). Pas de HTTP ici, pas de SQL brut ici.
"""
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import create_user, find_by_email


def register(first_name, email, password):
    """Inscrit un utilisateur. Renvoie (True, id) ou (False, message d'erreur)."""
    # 1. Refuser si l'email existe déjà
    if find_by_email(email):
        return False, "Cet email est déjà utilisé."

    # 2. Hasher le mot de passe (jamais en clair)
    password_hash = generate_password_hash(password)

    # 3. Créer l'utilisateur en base
    user_id = create_user(first_name, email, password_hash)
    return True, user_id


def login(email, password):
    """Vérifie les identifiants. Renvoie l'utilisateur (dict) si OK, sinon None."""
    user = find_by_email(email)

    if user is None:                      # email inconnu
        return None
    if not user["password_hash"]:         # compte Google (pas de mdp local)
        return None

    # Re-hasher le mdp tapé et comparer au hash stocké
    if not check_password_hash(user["password_hash"], password):
        return None

    return user
