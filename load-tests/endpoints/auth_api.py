"""
endpoints/auth_api.py

Low-level helpers for authentication API endpoints.

Each function accepts a Locust HTTP client and returns the parsed JSON response.
"""


def signup(client, payload: dict) -> dict:
    """
    POST /api/signup

    Register a new user account.

    Args:
        client: Locust HttpUser client
        payload: dict with keys 'name', 'email', 'password'

    Returns:
        Parsed JSON response body.
    """
    with client.post(
        "/api/signup",
        json=payload,
        name="/api/signup",
        catch_response=True,
    ) as response:
        if response.status_code == 201:
            response.success()
            return response.json()
        response.failure(f"Signup failed: {response.status_code} — {response.text}")
        return {}


def login(client, payload: dict) -> dict:
    """
    POST /api/login

    Authenticate an existing user and retrieve an access token.

    Args:
        client: Locust HttpUser client
        payload: dict with keys 'email', 'password'

    Returns:
        Parsed JSON response body (expected to contain 'access_token').
    """
    with client.post(
        "/api/login",
        json=payload,
        name="/api/login",
        catch_response=True,
    ) as response:
        if response.status_code == 200:
            response.success()
            return response.json()
        response.failure(f"Login failed: {response.status_code} — {response.text}")
        return {}
