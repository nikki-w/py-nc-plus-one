from src.connection import get_connection

# Tests for auth/login
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


# Tests for auth/register
def test_correct_details_successfully_registers_user(client):
    response = client.post("/auth/register",
                           json={"name": "Nikki Walker",
                                 "email": "nikki@example.com",
                                 "password": "password123",
                                 },)
    assert response.status_code == 201
    assert response.json()["user"]["name"] == "Nikki Walker"
    assert "password" or "password_hash" not in response.json()


def test_correct_user_details_successfuly_stores_user_in_databse(client):
    response = client.post("/auth/register",
                           json={"name": "Nikki Walker",
                                 "email": "nikki@example.com",
                                 "password": "password123",
                                 },)


    assert response.status_code == 201
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users;")
            rows = cur.fetchall()
    
        assert len(rows)==7
        assert rows[6][2] != "password123"
    finally:
        conn.close()


def test_missing_name_raises_error(client):
    response = client.post("/auth/register",
                           json={"name": "",
                                 "email": "carol@example.com",
                                 "password": "password1234",
                                 },)
    assert response.status_code == 400
    assert response.json()["detail"] == "Name is required."


def test_missing_email_raises_error(client):
    response = client.post("/auth/register",
                           json={"name": "Carol Singh",
                                 "email": "",
                                 "password": "password1234",
                                 },)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email is required."


def test_missing_password_raises_error(client):
    response = client.post("/auth/register",
                           json={"name": "Carol Singh",
                                 "email": "carol@example.com",
                                 "password": "",
                                 },)
    assert response.status_code == 400
    assert response.json()["detail"] == "Password is required."


def test_existing_email_raises_an_error(client):
    response = client.post("/auth/register",
                           json={"name": "Carol Singh",
                                 "email": "carol@example.com",
                                 "password": "password1234",
                                 },)
    assert response.status_code == 409
    assert response.json()["detail"] == "Email is already in use."
