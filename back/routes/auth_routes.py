from flask import Blueprint, request, jsonify, session

from controllers.auth_controller import register, login

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/api/register", methods=["POST"])
def route_register():
    data = request.get_json()
    first_name = data.get("first_name")
    email = data.get("email")
    password = data.get("password")

    success, result = register(first_name, email, password)
    if not success:
        return jsonify({"error": result}), 400

    # connexion auto apres inscription
    session["user_id"] = result
    session["first_name"] = first_name
    return jsonify({"message": "Inscription réussie", "first_name": first_name})


@auth_bp.route("/api/login", methods=["POST"])
def route_login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = login(email, password)
    if user is None:
        return jsonify({"error": "Email ou mot de passe incorrect."}), 401

    session["user_id"] = user["id"]
    session["first_name"] = user["first_name"]
    return jsonify({"message": "Connexion réussie", "first_name": user["first_name"]})


@auth_bp.route("/api/me", methods=["GET"])
def route_me():
    # le front demande qui est connecte
    if "user_id" not in session:
        return jsonify({"connected": False})
    return jsonify({"connected": True, "first_name": session.get("first_name")})


@auth_bp.route("/api/logout", methods=["POST"])
def route_logout():
    session.clear()
    return jsonify({"message": "Déconnecté"})
