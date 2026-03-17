"""
scenarios/user_signup_flow.py

High-level scenario: user signup followed by login.

This scenario is used in locustfile.py to simulate a new user registering
and immediately authenticating to obtain an access token.
"""

from endpoints.auth_api import signup, login
from utils.data_factory import make_user


def signup_and_login(client) -> str:
    """
    Simulate a new user signing up and logging in.

    Steps:
        1. Generate random user data.
        2. POST /api/signup
        3. POST /api/login
        4. Return the access token string (empty string if login fails).

    Args:
        client: Locust HttpUser client

    Returns:
        Access token string, or empty string on failure.
    """
    user = make_user()

    signup(client, {
        "name": user["name"],
        "email": user["email"],
        "password": user["password"],
    })

    response = login(client, {
        "email": user["email"],
        "password": user["password"],
    })

    return response.get("access_token", "")
