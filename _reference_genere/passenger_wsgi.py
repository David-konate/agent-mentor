# -*- coding: utf-8 -*-
"""
passenger_wsgi.py
=================
Point d'entree pour o2switch (hebergement mutualise cPanel + Passenger).

Passenger cherche AUTOMATIQUEMENT un fichier nomme "passenger_wsgi.py"
a la racine de l'application Python configuree dans cPanel, et y cherche
un objet WSGI nomme "application".

Ici, on importe simplement l'app Flask definie dans app.py.
"""

import sys
import os

# On s'assure que le dossier du projet est dans le chemin d'import.
sys.path.insert(0, os.path.dirname(__file__))

from app import app as application  # noqa: E402  (import apres modif du path)
