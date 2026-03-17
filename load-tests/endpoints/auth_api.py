"""
endpoints/auth_api.py

Low-level helpers for authentication API endpoints.

Each function accepts a Locust HTTP client and returns the parsed JSON response.
"""


def signup(client, payload: dict) -> dict:
    """
    POST /api/us/auth/register

    Register a new user account.

    Args:
        client: Locust HttpUser client
        payload: dict with keys 'name', 'email', 'password'

    Returns:
        Parsed JSON response body.
    """
    with client.post(
        "/api/us/auth/register",
        json=payload,
        name="/api/us/auth/register",
        catch_response=True,
    ) as response:
        if response.status_code == 201:
            response.success()
            return response.json()
        response.failure(f"Signup failed: {response.status_code} — {response.text}")
        return {}


def login(client, payload: dict) -> dict:
    """
    POST /api/us/auth/login

    Authenticate an existing user and retrieve an access token.

    Args:
        client: Locust HttpUser client
        payload: dict with keys 'email', 'password'

    Returns:
        Parsed JSON response body (expected to contain 'access_token').
    """
    with client.post(
        "/api/us/auth/login",
        json=payload,
        name="/api/us/auth/login",
        catch_response=True,
    ) as response:
        if response.status_code == 200:
            response.success()
            return response.json()
        response.failure(f"Login failed: {response.status_code} — {response.text}")
        return {}


def get_me(client, token: str) -> dict:
    """
    GET /api/us/users/me

    Retrieve current authenticated user profile.

    Args:
        client: Locust HttpUser client
        token: Bearer access token

    Returns:
        Parsed JSON response body.
    """
    headers = {"Authorization": f"Bearer {token}"}

    with client.get(
        "/api/us/users/me",
        headers=headers,
        name="/api/us/users/me",
        catch_response=True,
    ) as response:
        if response.status_code == 200:
            response.success()
            return response.json()
        response.failure(f"Get me failed: {response.status_code} — {response.text}")
        return {}
