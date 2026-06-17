import config
from flask import Flask, send_from_directory

from routes.chat_routes import chat_bp
from routes.auth_routes import auth_bp

app = Flask(__name__, static_folder=config.FRONT_DIR, static_url_path="")
app.secret_key = config.SECRET_KEY

app.register_blueprint(chat_bp)
app.register_blueprint(auth_bp)


@app.route("/")
def home():
    return send_from_directory(config.FRONT_DIR, "index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
