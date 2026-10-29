from src.connection import get_connection

def get_user(email: str) -> dict | None:
    """Returns user data when their email matches an existing user in the users table."""
    conn = get_connection()
    user_dict = None

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE email = %s;", (email,))
        columns = [desc[0] for desc in cur.description]
        row = cur.fetchone()

        if row:
            user_dict = dict(zip(columns, row))
            
    conn.close()
    return user_dict