# Load Testing — Locust

This directory contains all backend load tests for the KalyNow API using [Locust](https://locust.io/).

---

## Structure

```
load-tests/
├── locustfile.py          # Main entry point — defines user behaviors
├── endpoints/             # Low-level API call helpers (one file per domain)
│   ├── auth_api.py
│   ├── offer_api.py
│   └── restaurant_api.py
├── scenarios/             # High-level user flows composed from endpoints
│   ├── user_signup_flow.py
│   ├── user_profile_flow.py
│   └── create_offer_flow.py
└── utils/
    ├── http_client.py     # Shared HTTP client with response validation
    └── data_factory.py    # Fake data generator using Faker
```

---

## Running Tests

### With web UI

```bash
locust -f load-tests/locustfile.py --host=http://kalynow.mg
```

Open [http://localhost:8089](http://localhost:8089) to configure and start the test.

### Headless mode

```bash
locust -f load-tests/locustfile.py --host=http://kalynow.mg \
  --headless -u 10 -r 2 --run-time 60s
```

---

## Adding a New Scenario

1. Add an endpoint helper in `endpoints/` if needed.
2. Create a new scenario file in `scenarios/`.
3. Import and use the scenario in `locustfile.py` inside a `@task` method.

---

## Notes

- All endpoint helpers receive a Locust `client` object and return the parsed JSON response.
- Use `data_factory.py` to generate randomized test data per request.
- Avoid hardcoding credentials or URLs — use environment variables via `.env`.
- User-service endpoints must use the `/api/us` prefix (Traefik architecture).
- Signup is not part of load tests. Authentication uses only env credentials via `/api/us/auth/login`, then profile via `/api/us/users/me`.
- Offer-service endpoints must use the `/api/of` prefix.
- Current offer/restaurant flow covers:
  - Restaurant: `POST /api/of/restaurants`, `GET /api/of/restaurants`, `GET /api/of/restaurants/:id`, `PUT /api/of/restaurants/:id`
  - Offer: `POST /api/of/offers`, `GET /api/of/offers`, `GET /api/of/offers/:id`, `PUT /api/of/offers/:id`
- Seeing `Aggregated 0 0` at startup is normal before users are fully spawned.
