"""
endpoints/offer_api.py

Low-level helpers for offer API endpoints.
"""


def create_offer(client, payload: dict, token: str) -> dict:
    """
    POST /api/offers

    Create a new offer for a restaurant.

    Args:
        client: Locust HttpUser client
        payload: dict with offer data (title, description, discount, restaurant_id)
        token:   Bearer access token

    Returns:
        Parsed JSON response body.
    """
    headers = {"Authorization": f"Bearer {token}"}

    with client.post(
        "/api/offers",
        json=payload,
        headers=headers,
        name="/api/offers",
        catch_response=True,
    ) as response:
        if response.status_code == 201:
            response.success()
            return response.json()
        response.failure(
            f"Create offer failed: {response.status_code} — {response.text}"
        )
        return {}
