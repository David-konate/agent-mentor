from database import get_connection


def create_user(first_name, email, password_hash):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO users (first_name, email, password_hash) VALUES (%s, %s, %s)",
            (first_name, email, password_hash),
        )
        new_id = cur.lastrowid
    conn.close()
    return new_id


def find_by_email(email):
    conn = get_connection()
    with conn.cursor() as cur:
        # %s = requete parametree (anti injection sql)
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
    conn.close()
    return user
