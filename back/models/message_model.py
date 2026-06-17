from database import get_connection


def save_message(user_id, role, content):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO messages (user_id, role, content) VALUES (%s, %s, %s)",
            (user_id, role, content),
        )
    conn.close()


def get_messages(user_id):
    # tous les messages du user, du plus vieux au plus recent
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT role, content FROM messages WHERE user_id = %s ORDER BY created_at", (user_id,))
        messages = cur.fetchall()
    conn.close()
    return messages
