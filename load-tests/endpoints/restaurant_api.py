"""
endpoints/restaurant_api.py

Low-level helpers for restaurant API endpoints.
"""


def create_restaurant(client, payload: dict, token: str) -> dict:
    """
    POST /api/of/restaurants

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
        "/api/of/restaurants",
        json=payload,
        headers=headers,
        name="/api/of/restaurants",
        catch_response=True,
    ) as response:
        if response.status_code == 201:
            response.success()
            return response.json()
        response.failure(
            f"Create restaurant failed: {response.status_code} — {response.text}"
        )
        return {}


def get_restaurants(client, token: str, page: int = 1, limit: int = 10) -> dict:
    """
    GET /api/of/restaurants

    List restaurants (paginated).
    """
    headers = {"Authorization": f"Bearer {token}"}

    with client.get(
        f"/api/of/restaurants?page={page}&limit={limit}",
        headers=headers,
        name="/api/of/restaurants",
        catch_response=True,
    ) as response:
        if response.status_code == 200:
            response.success()
            return response.json()
        response.failure(
            f"Get restaurants failed: {response.status_code} — {response.text}"
        )
        return {}


def get_restaurant_by_id(client, restaurant_id: str, token: str) -> dict:
    """
    GET /api/of/restaurants/:id

    Fetch one restaurant by ID.
    """
    headers = {"Authorization": f"Bearer {token}"}

    with client.get(
        f"/api/of/restaurants/{restaurant_id}",
        headers=headers,
        name="/api/of/restaurants/:id",
        catch_response=True,
    ) as response:
        if response.status_code == 200:
            response.success()
            return response.json()
        response.failure(
            f"Get restaurant by id failed: {response.status_code} — {response.text}"
        )
        return {}


def update_restaurant(client, restaurant_id: str, payload: dict, token: str) -> dict:
    """
    PUT /api/of/restaurants/:id

    Update an existing restaurant.
    """
    headers = {"Authorization": f"Bearer {token}"}

    with client.put(
        f"/api/of/restaurants/{restaurant_id}",
        json=payload,
        headers=headers,
        name="/api/of/restaurants/:id",
        catch_response=True,
    ) as response:
        if response.status_code == 200:
            response.success()
            return response.json()
        response.failure(
            f"Update restaurant failed: {response.status_code} — {response.text}"
        )
        return {}
