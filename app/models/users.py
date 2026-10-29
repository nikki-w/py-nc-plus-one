from src.connection import get_connection
from src.passwords import hash_password

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


def check_if_email_exists(email: str) -> bool:
    """Checks if a user already exists in the database and returns a bool based on this."""
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE email = %s;", (email,))

        user = cur.fetchone()

    conn.close()

    if user is None:
        return False
    
    return True


def register_user(name: str, email: str, password: str) -> dict | None:
    """Registers a new user when they give a name, email and password."""
    conn = get_connection()
    user_dict = None
    password = hash_password(password)

    with conn.cursor() as cur:
        cur.execute("""INSERT INTO users 
                            (name, email, password_hash)
                        VALUES
                            (%s, %s, %s)
                        RETURNING id, name, email, created_at
                    """, (name.capitalize(), email, password))
        
        columns = [desc[0] for desc in cur.description]
        row = cur.fetchone()

        if row:
            user_dict = {"user": dict(zip(columns, row))}
    
    conn.close()

    return user_dict

