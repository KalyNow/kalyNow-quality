# kalyNow-quality

QA automation repository for the KalyNow project, combining backend load testing with Locust and end-to-end web and mobile testing using Robot Framework.

---

## Purpose

This repository provides a clean, extensible starting point for QA automation on the KalyNow platform. It is split into two main areas:

- **Load Testing** — Backend API performance tests using [Locust](https://locust.io/)
- **End-to-End Testing** — Web and mobile UI tests using [Robot Framework](https://robotframework.org/) with SeleniumLibrary and AppiumLibrary

The goal is NOT to ship a complete test suite. It is to provide a professional structure and simple examples that developers and QA engineers can extend over time.

---

## Project Structure

```
qa-automation/
├── README.md                        # This file
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variable template
│
├── load-tests/
│   ├── README.md                    # Load testing documentation
│   ├── locustfile.py                # Main Locust entry point
│   ├── endpoints/
│   │   ├── auth_api.py              # Auth endpoint helpers
│   │   ├── offer_api.py             # Offer endpoint helpers
│   │   └── restaurant_api.py        # Restaurant endpoint helpers
│   ├── scenarios/
│   │   ├── user_signup_flow.py      # Signup + login flow
│   │   └── create_offer_flow.py     # Restaurant + offer creation flow
│   └── utils/
│       ├── http_client.py           # Shared HTTP client wrapper
│       └── data_factory.py          # Fake test data generator
│
├── robot-tests/
│   ├── README.md                    # Robot Framework documentation
│   ├── resources/
│   │   ├── keywords/
│   │   │   ├── auth_keywords.robot  # Reusable auth keywords
│   │   │   └── offer_keywords.robot # Reusable offer keywords
│   │   └── pages/
│   │       ├── login_page.robot     # Login page object
│   │       └── home_page.robot      # Home page object
│   └── tests/
│       ├── web/
│       │   ├── login_test.robot         # Web login test
│       │   └── create_offer_test.robot  # Web create offer test
│       └── mobile/
│           └── login_mobile_test.robot  # Mobile login test (Appium)
│
└── scripts/
    ├── run_locust.sh                # Shell script to run Locust
    └── run_robot.sh                 # Shell script to run Robot Framework
```

---

## Installation

### Prerequisites

- Python 3.10+
- pip
- Google Chrome + ChromeDriver (for web tests)
- Appium server (for mobile tests)

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

```bash
cp .env.example .env
# Edit .env with your local values
```

---

## Running Load Tests

### Start Locust with web UI

```bash
locust -f load-tests/locustfile.py --host=http://localhost:8000
```

Then open [http://localhost:8089](http://localhost:8089) in your browser.

### Run headless (no web UI)

```bash
locust -f load-tests/locustfile.py --host=http://localhost:8000 --headless -u 10 -r 2
```

Or use the helper script:

```bash
bash scripts/run_locust.sh
```

---

## Running Robot Framework Tests

### Run all web tests

```bash
robot robot-tests/tests/web
```

### Run all mobile tests

```bash
robot robot-tests/tests/mobile
```

### Run a specific test file

```bash
robot robot-tests/tests/web/login_test.robot
```

Or use the helper script:

```bash
bash scripts/run_robot.sh
```

---

## Environment Variables

See `.env.example` for all supported variables. Key ones:

| Variable         | Description                         |
|------------------|-------------------------------------|
| `BASE_URL`       | Backend API base URL                |
| `WEB_URL`        | Frontend web app URL                |
| `BROWSER`        | Browser for Selenium (default: chrome) |
| `APPIUM_URL`     | Appium server URL for mobile tests  |

---

## Extending the Project

- Add new load test scenarios in `load-tests/scenarios/`
- Add new endpoint helpers in `load-tests/endpoints/`
- Add new Robot Framework keywords in `robot-tests/resources/keywords/`
- Add new test cases in `robot-tests/tests/web/` or `robot-tests/tests/mobile/`
