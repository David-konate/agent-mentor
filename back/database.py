# -*- coding: utf-8 -*-
"""
database.py
===========
Connexion à la base MySQL (MAMP) + création des tables.
"""
import pymysql
import config


def get_connection():
    """Ouvre une connexion à la base MySQL (MAMP)."""
    return pymysql.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME,
        cursorclass=pymysql.cursors.DictCursor,  # résultats en dict {colonne: valeur}
        autocommit=True,                          # chaque requête est enregistrée direct
    )


def init_db():
    """Crée les tables si elles n'existent pas encore."""
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password_hash VARCHAR(255),
                google_id VARCHAR(255) UNIQUE
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                role VARCHAR(20) NOT NULL,
                content TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
    conn.close()
    print("Tables créées (ou déjà existantes).")


if __name__ == "__main__":
    init_db()
