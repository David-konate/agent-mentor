from flask import Blueprint, request, jsonify, session

from controllers.chat_controller import handle_chat, get_history

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/api/chat", methods=["POST"])
def chat():
    # faut etre connecte
    if "user_id" not in session:
        return jsonify({"error": "Tu dois être connecté."}), 401

    data = request.get_json()
    mode = data.get("mode", "tutor")
    lang = data.get("lang", "fr")
    messages = data.get("messages", [])

    response = handle_chat(session["user_id"], session.get("first_name"), mode, lang, messages)
    return jsonify({"response": response})


@chat_bp.route("/api/history", methods=["GET"])
def history():
    if "user_id" not in session:
        return jsonify({"error": "Tu dois être connecté."}), 401

    messages = get_history(session["user_id"])
    return jsonify({"messages": messages})
