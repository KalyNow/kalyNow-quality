"""
endpoints/restaurant_api.py

Low-level helpers for restaurant API endpoints.
"""


def create_restaurant(client, payload: dict, token: str) -> dict:
    """
    POST /api/restaurants

    Create a new restaurant.

    Args:
        client:  Locust HttpUser client
        payload: dict with restaurant data (name, address, category)
        token:   Bearer access token

    Returns:
        Parsed JSON response body.
    """
    headers = {"Authorization": f"Bearer {token}"}

    with client.post(
        "/api/restaurants",
        json=payload,
        headers=headers,
        name="/api/restaurants",
        catch_response=True,
    ) as response:
        if response.status_code == 201:
            response.success()
            return response.json()
        response.failure(
            f"Create restaurant failed: {response.status_code} — {response.text}"
        )
        return {}
