"""
endpoints/offer_api.py

Low-level helpers for offer API endpoints.
"""


def create_offer(client, payload: dict, token: str) -> dict:
    """
    POST /api/of/offers

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
        "/api/of/offers",
        json=payload,
        headers=headers,
        name="/api/of/offers",
        catch_response=True,
    ) as response:
        if response.status_code == 201:
            response.success()
            return response.json()
        response.failure(
            f"Create offer failed: {response.status_code} — {response.text}"
        )
        return {}


def get_offers(client, token: str, page: int = 1, limit: int = 10, restaurant_id: str | None = None) -> dict:
    """
    GET /api/of/offers

    List offers (paginated), optionally filtered by restaurantId.
    """
    headers = {"Authorization": f"Bearer {token}"}
    query = f"page={page}&limit={limit}"
    if restaurant_id:
        query += f"&restaurantId={restaurant_id}"

    with client.get(
        f"/api/of/offers?{query}",
        headers=headers,
        name="/api/of/offers",
        catch_response=True,
    ) as response:
        if response.status_code == 200:
            response.success()
            return response.json()
        response.failure(
            f"Get offers failed: {response.status_code} — {response.text}"
        )
        return {}


def get_offer_by_id(client, offer_id: str, token: str) -> dict:
    """
    GET /api/of/offers/:id

    Fetch one offer by ID.
    """
    headers = {"Authorization": f"Bearer {token}"}

    with client.get(
        f"/api/of/offers/{offer_id}",
        headers=headers,
        name="/api/of/offers/:id",
        catch_response=True,
    ) as response:
        if response.status_code == 200:
            response.success()
            return response.json()
        response.failure(
            f"Get offer by id failed: {response.status_code} — {response.text}"
        )
        return {}


def update_offer(client, offer_id: str, payload: dict, token: str) -> dict:
    """
    PUT /api/of/offers/:id

    Update an existing offer.
    """
    headers = {"Authorization": f"Bearer {token}"}

    with client.put(
        f"/api/of/offers/{offer_id}",
        json=payload,
        headers=headers,
        name="/api/of/offers/:id",
        catch_response=True,
    ) as response:
        if response.status_code == 200:
            response.success()
            return response.json()
        response.failure(
            f"Update offer failed: {response.status_code} — {response.text}"
        )
        return {}
