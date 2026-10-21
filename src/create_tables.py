"""File containing function that creates all database tables for nc_plus_one database."""

from psycopg2.extensions import connection

def create_users_table(conn: connection) -> None:
    """Creates users database table in the nc_plus_one database."""
    with conn.cursor() as cursor:

        create_users_table = """
                            CREATE TABLE users (
                                id INT GENERATED ALWAYS AS IDENTITY,
                                email VARCHAR(255) UNIQUE NOT NULL,
                                password VARCHAR(255) NOT NULL,
                                name VARCHAR(255) NOT NULL,
                                created_at TIMESTAMPTZ DEFAULT NOW(),
                                PRIMARY KEY (id)
                            );
                        """

        cursor.execute(create_users_table)
        conn.commit()


def create_venues_table(conn: connection) -> None:
    """Creates venues database table in the nc_plus_one database."""
    with conn.cursor() as cursor:

        create_venues_table = """
                            CREATE TABLE venues (
                                id INT GENERATED ALWAYS AS IDENTITY,
                                name VARCHAR(255) NOT NULL,
                                address TEXT,
                                capacity INT,
                                PRIMARY KEY (id)
                            );
                            """

        cursor.execute(create_venues_table)
        conn.commit()


def create_events_table(conn: connection) -> None:
    """Creates events database table in the nc_plus_one database."""
    with conn.cursor() as cursor:

        create_events_table = """
                            CREATE TABLE events (
                                id INT GENERATED ALWAYS AS IDENTITY,
                                title VARCHAR(255) NOT NULL,
                                description VARCHAR(255),
                                starts_at TIMESTAMPTZ NOT NULL,
                                ends_at TIMESTAMPTZ NOT NULL,
                                organiser_id INT,
                                venue_id INT,
                                created_at TIMESTAMPTZ DEFAULT NOW(),
                                PRIMARY KEY (id),
                                FOREIGN KEY (organiser_id) REFERENCES Users(id),
                                FOREIGN KEY (venue_id) REFERENCES Venues(id)
                            );
                            """

        cursor.execute(create_events_table)
        conn.commit()


def create_rsvps_table(conn: connection) -> None:
    """Creates rsvps database table in the nc_plus_one database."""
    with conn.cursor() as cursor:

        create_rsvps_table = """
                            CREATE TABLE rsvps (
                                id INT GENERATED ALWAYS AS IDENTITY,
                                attendee_id INT,
                                event_id INT,
                                created_at TIMESTAMPTZ DEFAULT NOW(),
                                PRIMARY KEY (id),
                                FOREIGN KEY (attendee_id) REFERENCES Users(id),
                                FOREIGN KEY (event_id) REFERENCES Events(id)
                            );      
                            """

        cursor.execute(create_rsvps_table)
        conn.commit()


def create_tables(conn: connection) -> None:
    """Creates all database tables from the nc_plus_one database."""
    create_users_table(conn)
    create_venues_table(conn)
    create_events_table(conn)
    create_rsvps_table(conn)