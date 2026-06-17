# -*- coding: utf-8 -*-
"""
utilisateur_model.py  (couche MODEL)
====================================
Accès aux données de la table `utilisateurs` (le SQL, rien d'autre).
"""
from database import get_connexion


def creer_utilisateur(prenom, email, mot_de_passe_hash):
    """Insère un nouvel utilisateur et renvoie son id."""
    conn = get_connexion()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO utilisateurs (prenom, email, mot_de_passe_hash) VALUES (%s, %s, %s)",
            (prenom, email, mot_de_passe_hash),
        )
        nouvel_id = cur.lastrowid        # l'id auto-généré de la ligne insérée
    conn.close()
    return nouvel_id


def trouver_par_email(email):
    """Renvoie l'utilisateur ayant cet email (un dict), ou None s'il n'existe pas."""
    conn = get_connexion()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM utilisateurs WHERE email = %s", (email,))
        utilisateur = cur.fetchone()     # une seule ligne (ou None)
    conn.close()
    return utilisateur