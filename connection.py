import os
import psycopg2

from dotenv import load_dotenv

def get_connection():

    load_dotenv()

    if not os.getenv("PGDATABASE"):
        raise RuntimeError("PGDATABASE NOT SET")

    connection = psycopg2.connect()
    return connection

