"""
utils/data_factory.py

Generates randomized fake test data using the Faker library.

Using random data per request prevents duplicate-key errors and makes
each simulated user appear unique to the backend.
"""

from faker import Faker

fake = Faker()


def make_user() -> dict:
    """
    Generate a random user payload.

    Returns:
        dict with keys: name, email, password
    """
    return {
        "name": fake.name(),
        "email": fake.unique.email(),
        "password": "Test" + fake.password(length=10, special_chars=False),
    }


def make_restaurant() -> dict:
    """
    Generate a random restaurant payload.

    Returns:
        dict with keys: name, address, category
    """
    categories = ["Italian", "Japanese", "Mexican", "French", "American", "Thai"]
    return {
        "name": fake.company(),
        "address": fake.address().replace("\n", ", "),
        "category": fake.random_element(categories),
    }


def make_offer(restaurant_id: str) -> dict:
    """
    Generate a random offer payload for a given restaurant.

    Args:
        restaurant_id: ID of the restaurant this offer belongs to.

    Returns:
        dict with keys: restaurantId, title, description, price, discountedPrice
    """
    price = round(fake.pyfloat(left_digits=2, right_digits=2, positive=True, min_value=5, max_value=80), 2)
    discounted = round(price * fake.random_int(min=60, max=95) / 100, 2)

    return {
        "restaurantId": restaurant_id,
        "title": fake.catch_phrase(),
        "description": fake.sentence(),
        "price": price,
        "discountedPrice": discounted,
    }
