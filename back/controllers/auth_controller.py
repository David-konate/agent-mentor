from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import create_user, find_by_email


def register(first_name, email, password):
    # email deja pris ?
    if find_by_email(email):
        return False, "Cet email est déjà utilisé."

    # on hash le mdp avant de stocker
    password_hash = generate_password_hash(password)
    user_id = create_user(first_name, email, password_hash)
    return True, user_id


def login(email, password):
    user = find_by_email(email)
    if user is None:
        return None
    if not user["password_hash"]:   # compte google -> pas de mdp local
        return None
    # on compare le mdp tape au hash stocke
    if not check_password_hash(user["password_hash"], password):
        return None
    return user
