# -*- coding: utf-8 -*-
"""
app.py  (POINT D'ENTRÉE)
========================
Crée l'application Flask, la configure, et branche les routes (blueprints).
"""

import config  # charge le .env + la config EN PREMIER

from flask import Flask, send_from_directory

from routes.chat_routes import chat_bp
from routes.auth_routes import auth_bp

# Crée l'application web. Le front est servi depuis le dossier front/.
app = Flask(__name__, static_folder=config.FRONT_DIR, static_url_path="")

# Clé qui signe les sessions (sécurité).
app.secret_key = config.SECRET_KEY

# Branche les routes (blueprints) sur l'application.
app.register_blueprint(chat_bp)
app.register_blueprint(auth_bp)


@app.route("/")
def home():
    # Sert la page de chat (front/index.html).
    return send_from_directory(config.FRONT_DIR, "index.html")


if __name__ == "__main__":
    # Lancement en local. Sur o2switch, c'est passenger_wsgi.py qui démarre l'app.
    app.run(host="127.0.0.1", port=5000, debug=True)
