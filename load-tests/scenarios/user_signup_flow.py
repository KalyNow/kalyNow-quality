"""
scenarios/user_signup_flow.py

High-level authentication flow for load tests (login-only).

Signup is intentionally NOT tested here.
All virtual users authenticate using credentials from environment variables.
"""

import os

from dotenv import load_dotenv

from endpoints.auth_api import login

load_dotenv()


def _get_test_credentials() -> tuple[str, str]:
    """Return test credentials from environment variables or .env file."""
    email = os.getenv("TEST_USER_EMAIL", "").strip()
    password = os.getenv("TEST_USER_PASSWORD", "").strip()
    return email, password


def signup_and_login(client, use_env_credentials: bool = True) -> str:
    """
    Authenticate a user with environment credentials and return an access token.

    Steps:
        1. Read `TEST_USER_EMAIL` and `TEST_USER_PASSWORD`.
        2. POST /api/us/auth/login.
        3. Return the access token string (empty string on failure).

    Args:
        client: Locust HttpUser client

    Returns:
        Access token string, or empty string on failure.
    """
    if not use_env_credentials:
        return ""

    email, password = _get_test_credentials()
    if not email or not password:
        return ""

    response = login(client, {
        "email": email,
        "password": password,
    })

    return response.get("accessToken", "") or response.get("access_token", "")
