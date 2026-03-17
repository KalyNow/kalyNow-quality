"""
scenarios/user_profile_flow.py

High-level scenario: fetch authenticated user profile from user-service.
"""

from endpoints.auth_api import get_me


def fetch_my_profile(client, token: str) -> None:
    """
    Simulate an authenticated user requesting their profile.

    Args:
        client: Locust HttpUser client
        token: Bearer access token
    """
    if not token:
        return

    get_me(client, token)
