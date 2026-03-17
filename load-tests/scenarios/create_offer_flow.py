"""
scenarios/create_offer_flow.py

High-level scenario covering create/get/update for restaurants and offers.

Requires an authenticated user (access token).
"""

from endpoints.restaurant_api import (
    create_restaurant,
    get_restaurants,
    get_restaurant_by_id,
    update_restaurant,
)
from endpoints.offer_api import (
    create_offer,
    get_offers,
    get_offer_by_id,
    update_offer,
)
from utils.data_factory import make_restaurant, make_offer


def create_restaurant_and_offer(client, token: str) -> None:
    """
    Simulate a restaurant owner running a CRUD-like happy path.

    Steps:
        1. Generate random restaurant data.
        2. POST /api/of/restaurants
        3. GET /api/of/restaurants
        4. GET /api/of/restaurants/:id
        5. PUT /api/of/restaurants/:id
        6. Create multiple offers (2-3) linked to the same restaurant.
           For each offer:
           - Generate random offer data
           - POST /api/of/offers
           - GET /api/of/offers/:id
           - PUT /api/of/offers/:id
        7. GET /api/of/offers (filter by restaurant)

    Args:
        client: Locust HttpUser client
        token:  Bearer access token for the authenticated user
    """
    restaurant_data = make_restaurant()
    restaurant = create_restaurant(client, restaurant_data, token)

    # Extract restaurant ID from creation response (supports both 'id' and '_id')
    restaurant_id = restaurant.get("id") or restaurant.get("_id")
    if not restaurant_id:
        print(f"[DEBUG] Restaurant creation failed or no ID in response: {restaurant}")
        return

    get_restaurants(client, token)
    get_restaurant_by_id(client, restaurant_id, token)
    update_restaurant(client, restaurant_id, {
        "description": f"Updated by load-test for {restaurant_data['name']}",
        "isActive": True,
    }, token)

    # Create 2-3 offers for the same restaurant
    num_offers = 2  # Create 2 offers per restaurant (can change to 3 for more variety)
    for i in range(num_offers):
        offer_data = make_offer(restaurant_id)
        offer = create_offer(client, offer_data, token)

        # Extract offer ID from creation response (supports both 'id' and '_id')
        offer_id = offer.get("id") or offer.get("_id")
        if not offer_id:
            print(f"[DEBUG] Offer {i+1} creation failed or no ID in response: {offer}")
            continue

        get_offer_by_id(client, offer_id, token)
        update_offer(client, offer_id, {
            "description": f"Updated offer {i+1} by load-test",
            "discountedPrice": offer_data["discountedPrice"],
            "isActive": True,
        }, token)

    # Get all offers for this restaurant
    get_offers(client, token, restaurant_id=restaurant_id)
