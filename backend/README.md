# NC Plus One Project

## Project Overview:

NC Plus One is a backend REST API designed for an events platform. It acts as the core data layer for a full-stack application, managing user actions, organiser tools, and data integrity. This project is built with frontend consumption in mind, focusing on clean engineering practices, security, and strict data validation.


## Database Setup:

**Requirements**
* `psql` is installed
* A `.env` file should be created with your own credentials, an example of what's required is available to view in `.env.example`

**Setup**

Start by creating a virtual environment:

`python -m venv .venv`
`source .venv/bin/activate`

Install any requirements from `requirements.txt`:

`pip install -r requirements.txt`

Create a `.env` (an example of the format can be found in the file `.env.example`):

`touch .env`

To set up the database and seed it with data run the following commands:

`psql -U [USERNAME] -f db/setup.sql`
`python src/seed_functions.py`

In a different terminal start up the API by running the folowing:

`uvicorn app.main:app --reload`

---
**_Note on testing:_**

Tests have been created to ensure functions and endpoints work as expected. To be able to use these tests, you will need to create a `.env.test` (using the same credentials except for `PGATABASE` which should end in `_test`) and a seperate database for testing. This can be done using the follwoing commands:

`touch .env.test`
`psql -U [USERNAME] -f db/test_setup.sql`
`python src/seed_functions.py`

Tests can then be ran using `pytest` in the terminal.