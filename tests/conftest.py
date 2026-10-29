import os
import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from app.main import app
from src.connection import get_connection
from src.seed_functions import seed


os.environ["ENV"] = "test"

load_dotenv(dotenv_path=".env.test", override=True)

@pytest.fixture(autouse=True)
def seed_test_db():
    database = os.getenv("PGDATABASE", "")
    assert database.endswith("_test"), f"Refusing to seed non-test database {database!r}"

    with get_connection() as conn:
        seed(conn)

@pytest.fixture
def client():
    return TestClient(app)