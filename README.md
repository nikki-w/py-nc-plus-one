# NC Plus One Project

## Project Overview:

NC Plus One is a backend REST API designed for an events platform. It acts as the core data layer for a full-stack application, managing user actions, organiser tools, and data integrity. This project is built with frontend consumption in mind, focusing on clean engineering practices, security, and strict data validation.


## Database Setup:

**Requirements**
* `psql` is installed
* A `.env` file should be created with your own credentials, an example of what's required is available to view in `.env.example`

**Setup**

To set up the database run the following command:

`psql -U [USERNAME] -f db/setup.sql`

