import json
from connection import get_connection

def load_data_from_json(data_name):
    with open(f"db/data/{data_name}.json") as file:
        data = json.load(file)
    return data

def drop_tables(conn):
    with conn.cursor() as cursor:

        drop_tables =   """
                        DROP TABLE IF EXISTS users CASCADE;
                        DROP TABLE IF EXISTS venues CASCADE;
                        DROP TABLE IF EXISTS events CASCADE;
                        DROP TABLE IF EXISTS rsvps;
                        """

        cursor.execute(drop_tables)
        conn.commit()


def create_tables(conn):
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


def seed_user_data(conn, user_data):
    with conn.cursor() as cursor:

        seed_user_data = """
                        INSERT INTO users 
                            (email, password, name)
                        VALUES 
                            (%s, %s, %s);
                        """

        for data in user_data:
            cursor.execute(seed_user_data, (data["email"], data["password"], data["name"]))
            conn.commit()


def seed(conn):
    drop_tables(conn)
    create_tables(conn)
    user_data = load_data_from_json("users")
    seed_user_data(conn, user_data)


if __name__ == "__main__":
    conn = get_connection()
    seed(conn)