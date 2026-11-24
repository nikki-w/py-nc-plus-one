"""File containing function that drops all database tables."""

from psycopg2.extensions import connection

def drop_users_table(conn: connection) -> None:
    """Drops users tables from the nc_plus_one database."""
    with conn.cursor() as cursor:

        drop_users_table =   """
                        DROP TABLE IF EXISTS users CASCADE;
                        """

        cursor.execute(drop_users_table)
        conn.commit()


def drop_venues_table(conn: connection) -> None:
    """Drops venues tables from the nc_plus_one database."""
    with conn.cursor() as cursor:

        drop_venues_table =   """
                        DROP TABLE IF EXISTS venues CASCADE;
                        """

        cursor.execute(drop_venues_table)
        conn.commit()


def drop_events_table(conn: connection) -> None:
    """Drops events tables from the nc_plus_one database."""
    with conn.cursor() as cursor:

        drop_events_table =   """
                        DROP TABLE IF EXISTS events CASCADE;
                        """

        cursor.execute(drop_events_table)
        conn.commit()


def drop_rsvps_table(conn: connection) -> None:
    """Drops rsvps tables from the nc_plus_one database."""
    with conn.cursor() as cursor:

        drop_rsvps_table =   """
                        DROP TABLE IF EXISTS rsvps CASCADE;
                        """

        cursor.execute(drop_rsvps_table)
        conn.commit()


def drop_tables(conn: connection) -> None:
    """Drops all database tables from the nc_plus_one database."""
    drop_users_table(conn)
    drop_venues_table(conn)
    drop_events_table(conn)
    drop_rsvps_table(conn)
