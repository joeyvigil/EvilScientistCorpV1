from fastapi.testclient import TestClient

from app.main import app

# Create a TestClient so we can test our routes with HTTP requests
# Notice we're wrapping app from main.py with this
client = TestClient(app)

# This test suite tests create_user. We'll see a green test, red test, and a mocked test
# Green test - test that the function behaves as expect with valid user input
# Red test - test that the function raises the appropriate exception etc. with INVALID user input
# Mocked test - We'll use a "mock" for the user database so we don't manipulate real data


# Green test
def test_create_user_success():

    # Send a real POST request to create a user, and save the response
    response = client.post(
        "/users/", # the endpoint create_user() lives at
        json={
            "username":"testuser",
            "password":"testpassword",
            "email":"testemail@email.com"
        }
    )

    # Assert that the response is what we expect (status code, message, returned data)
    assert response.status_code == 201