"""File containing a function that connects to a database"""

import os
import psycopg2

from dotenv import load_dotenv

def get_connection() -> None:
    """Establishes a database connection."""
    load_dotenv()

    if not os.getenv("PGDATABASE"):
        raise RuntimeError("PGDATABASE not set in .env.")

    connection = psycopg2.connect()
    return connection

