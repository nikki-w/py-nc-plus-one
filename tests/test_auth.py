from src.connection import get_connection


def test_correct_details_returns_access_token(client):
    response = client.post("/auth/login",
                           json={"email": "alice@example.com",
                                 "password": "password123",
                                 },)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert isinstance(response.json()["access_token"], str)


def test_missing_email_returns_400(client):
    response = client.post("/auth/login",
                                json={"email": "",
                                        "password": "password123",
                                        },)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email is required."


def test_incorrect_email_returns_401(client):
    response = client.post("/auth/login",
                                json={"email": "test@example.com",
                                        "password": "password123",
                                        },)
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect email or password"


def test_missing_password_returns_400(client):
    response = client.post("/auth/login",
                               json={"email": "alice@example.com",
                                     "password": "",
                                     },)
    assert response.status_code == 400
    assert response.json()["detail"] == "Password is required."


def test_incorrect_password_returns_401(client):
    response = client.post("/auth/login",
                               json={"email": "alice@example",
                                     "password": "totallysafepassword",
                                     },)
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect email or password"