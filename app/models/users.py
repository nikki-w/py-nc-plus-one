from src.connection import get_connection


def get_user(email: str) -> dict:
    """Returns user data when their email matches an existing user in the users table."""
    with get_connection() as conn:
        user = conn.execute("SELECT * FROM users WHERE email = %s", (email,)).fetchone()
        conn.commit()
    return user