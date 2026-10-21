from src.connection import get_connection
from src.seed_functions import seed


if __name__ == "__main__":
    conn = get_connection()
    seed(conn)