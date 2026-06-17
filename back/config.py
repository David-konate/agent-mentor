import os
from dotenv import load_dotenv

# racine du projet (le dossier au dessus de back/)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(ROOT, ".env"))

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-a-changer-en-prod")

# config bdd
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
DB_PORT = int(os.environ.get("DB_PORT", 3306))
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "root")
DB_NAME = os.environ.get("DB_NAME", "mentor_cda")

FRONT_DIR = os.path.join(ROOT, "front")
