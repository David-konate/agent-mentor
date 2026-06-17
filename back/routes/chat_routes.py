# -*- coding: utf-8 -*-
"""
chat_routes.py  (couche ROUTE)
==============================
Gère le HTTP : reçoit la requête, appelle le controller, renvoie le JSON.
"""
from flask import Blueprint, request, jsonify, session

from controllers.chat_controller import handle_chat, get_history

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/api/chat", methods=["POST"])
def chat():
    # 🔒 Refuser si personne n'est connecté
    if "user_id" not in session:
        return jsonify({"error": "Tu dois être connecté."}), 401

    data = request.get_json()
    mode = data.get("mode", "tutor")
    messages = data.get("messages", [])

    # On passe le user_id (depuis la session) pour lier l'échange à l'utilisateur
    response = handle_chat(session["user_id"], session.get("first_name"), mode, messages)
    return jsonify({"response": response})


@chat_bp.route("/api/history", methods=["GET"])
def history():
    # 🔒 Réservé aux connectés
    if "user_id" not in session:
        return jsonify({"error": "Tu dois être connecté."}), 401

    messages = get_history(session["user_id"])
    return jsonify({"messages": messages})