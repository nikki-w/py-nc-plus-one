"""File containing a function that loads data from a json file."""

import json

def load_data_from_json(data_name: str) -> list[dict]:
    """Loads data from a json file."""
    with open(f"./db/data/{data_name}.json") as file:
        data = json.load(file)
    return data