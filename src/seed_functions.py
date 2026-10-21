"""File containing functions to seed the data in the nc_plus_one database."""

from .load_json import load_data_from_json
from .drop_tables import drop_tables
from .create_tables import create_tables
from psycopg2.extensions import connection

def seed_user_data(conn: connection, user_data: list[dict]) -> None:
    """Seeds data into the users table in nc_plus_one database."""
    with conn.cursor() as cursor:

        seed_user_data_to_table =  """
                                    INSERT INTO users 
                                        (email, password, name)
                                    VALUES 
                                        (%s, %s, %s);
                                    """

        for data in user_data:
            cursor.execute(seed_user_data_to_table, (data["email"], data["password"], data["name"]))
            conn.commit()


def seed_venue_data(conn: connection, venue_data: list[dict]) -> None:
    """Seeds data into the venues table in nc_plus_one database."""
    with conn.cursor() as cursor:

        seed_venue_data_to_table = """
                                    INSERT INTO venues
                                        (name, address, capacity)
                                    VALUES 
                                        (%s, %s, %s);
                                    """

        for data in venue_data:
            cursor.execute(seed_venue_data_to_table, (data["name"], data["address"], data["capacity"]))
            conn.commit()


def seed_event_data(conn: connection, event_data: list[dict]) -> None:
    """Seeds data into the events table in nc_plus_one database."""
    with conn.cursor() as cursor:

        seed_event_data_to_table = """
                                    INSERT INTO events
                                        (title, description, starts_at, ends_at, organiser_id, venue_id)
                                    VALUES 
                                        (%s, %s, %s, %s, %s, %s)
                                    ;
                                    """

        for data in event_data:
            cursor.execute(seed_event_data_to_table, 
                           (data["title"], data["description"], data["starts_at"], data["ends_at"], data["organiser_id"], data["venue_id"]))
            conn.commit()


def seed_rsvp_data(conn: connection, rsvp_data: list[dict]) -> None:
    """Seeds data into the rsvps table in nc_plus_one database."""
    with conn.cursor() as cursor:

        seed_rsvp_data_to_table = """
                                    INSERT INTO rsvps
                                        (attendee_id, event_id)
                                    VALUES 
                                        (%s, %s)
                                    ;
                                    """

        for data in rsvp_data:
            cursor.execute(seed_rsvp_data_to_table, 
                           (data["attendee_id"], data["event_id"]))
            conn.commit()


def seed(conn: connection) -> None:
    """Drops any existing tables, creates tables and 
    then seeds data into all tables of the nc_plus_one database."""
    # Drop any existing tables and then create them from scratch
    drop_tables(conn)
    create_tables(conn)

    # Load all json data
    user_data = load_data_from_json("users")
    venue_data = load_data_from_json("venues")
    event_data = load_data_from_json("events")
    rsvp_data = load_data_from_json("rsvps")

    # Seed data into the tables
    seed_user_data(conn, user_data)
    seed_venue_data(conn, venue_data)
    seed_event_data(conn, event_data)
    seed_rsvp_data(conn, rsvp_data)

