"""File containing function that creates all database tables for nc_plus_one database."""

from psycopg2.extensions import connection

def create_tables(conn: connection) -> None:
    """Loads all database tables from the nc_plus_one database."""
    with conn.cursor() as cursor:

        create_tables = """
                            CREATE TABLE users (
                                id INT GENERATED ALWAYS AS IDENTITY,
                                email VARCHAR(255) UNIQUE NOT NULL,
                                password VARCHAR(255) NOT NULL,
                                name VARCHAR(255) NOT NULL,
                                created_at TIMESTAMPTZ DEFAULT NOW(),
                                PRIMARY KEY (id)
                            );

                            CREATE TABLE venues (
                                id INT GENERATED ALWAYS AS IDENTITY,
                                name VARCHAR(255) NOT NULL,
                                address TEXT,
                                capacity INT,
                                PRIMARY KEY (id)
                            );                            
                                
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

        cursor.execute(create_tables)
        conn.commit()