"""
utils/http_client.py

Shared HTTP client helpers.

These utilities wrap common Locust request patterns so that endpoint
files stay clean and consistent.
"""


def post(client, url: str, payload: dict, token: str = "", name: str = "") -> dict:
    """
    Perform an authenticated or anonymous POST request.

    Args:
        client:  Locust HttpUser client
        url:     Endpoint path (e.g. '/api/offers')
        payload: Request body as dict (serialized to JSON)
        token:   Optional Bearer access token
        name:    Locust stats label (defaults to url)

    Returns:
        Parsed JSON response body, or empty dict on failure.
    """
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    with client.post(
        url,
        json=payload,
        headers=headers,
        name=name or url,
        catch_response=True,
    ) as response:
        if response.status_code in (200, 201):
            response.success()
            return response.json()
        response.failure(f"POST {url} failed: {response.status_code} — {response.text}")
        return {}
