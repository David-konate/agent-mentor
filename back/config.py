# -*- coding: utf-8 -*-
"""
config.py
=========
Configuration centrale de l'application + chargement du .env.
On calcule les chemins par rapport à la racine du projet (un niveau au-dessus
de back/), pour que ça marche quel que soit l'endroit d'où on lance l'app.
"""

import os
from dotenv import load_dotenv

# Racine du projet = le dossier parent de back/
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Charge les variables du .env (clé Groq, etc.) depuis la racine
load_dotenv(os.path.join(ROOT, ".env"))

# Clé secrète qui SIGNE les sessions (infalsifiable).
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-a-changer-en-prod")

# Connexion à la base de données MySQL (MAMP en local, MySQL sur o2switch).
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
DB_PORT = int(os.environ.get("DB_PORT", 3306))
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "root")
DB_NAME = os.environ.get("DB_NAME", "mentor_cda")

# Dossier du front (servi par Flask).
FRONT_DIR = os.path.join(ROOT, "front")
