"""File containing function that drops all database tables."""

from psycopg2.extensions import connection

def drop_tables(conn: connection) -> None:
    """Drops all database tables from the nc_plus_one database."""
    with conn.cursor() as cursor:

        drop_tables =   """
                        DROP TABLE IF EXISTS users CASCADE;
                        DROP TABLE IF EXISTS venues CASCADE;
                        DROP TABLE IF EXISTS events CASCADE;
                        DROP TABLE IF EXISTS rsvps;
                        """

        cursor.execute(drop_tables)
        conn.commit()
