"""
scenarios/create_offer_flow.py

High-level scenario: create a restaurant and then create an offer for it.

Requires an authenticated user (access token).
"""

from endpoints.restaurant_api import create_restaurant
from endpoints.offer_api import create_offer
from utils.data_factory import make_restaurant, make_offer


def create_restaurant_and_offer(client, token: str) -> None:
    """
    Simulate a restaurant owner creating a restaurant and publishing an offer.

    Steps:
        1. Generate random restaurant data.
        2. POST /api/restaurants
        3. Generate random offer data linked to the new restaurant.
        4. POST /api/offers

    Args:
        client: Locust HttpUser client
        token:  Bearer access token for the authenticated user
    """
    restaurant_data = make_restaurant()
    restaurant = create_restaurant(client, restaurant_data, token)

    restaurant_id = restaurant.get("id")
    if not restaurant_id:
        return

    offer_data = make_offer(restaurant_id)
    create_offer(client, offer_data, token)
