-- Setup script for the nc_plus_one_database

DROP DATABASE nc_plus_one;
CREATE DATABASE nc_plus_one;

\c nc_plus_one

CREATE TABLE IF NOT EXISTS Users (
    id INT GENERATED ALWAYS AS IDENTITY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Venues (
    id INT GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(255) NOT NULL,
    address TEXT,
    capacity INT,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Events (
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

CREATE TABLE IF NOT EXISTS Rsvps (
    id INT GENERATED ALWAYS AS IDENTITY,
    attendee_id INT,
    event_id INT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (id),
    FOREIGN KEY (attendee_id) REFERENCES Users(id),
    FOREIGN KEY (event_id) REFERENCES Events(id)
);