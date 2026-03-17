# Robot Framework Tests

This directory contains all end-to-end tests for the KalyNow platform using [Robot Framework](https://robotframework.org/).

---

## Structure

```
robot-tests/
├── resources/
│   ├── keywords/
│   │   ├── auth_keywords.robot    # Reusable login/logout keywords
│   │   └── offer_keywords.robot   # Reusable offer management keywords
│   └── pages/
│       ├── login_page.robot       # Login page locators and actions
│       └── home_page.robot        # Home page locators and actions
└── tests/
    ├── web/
    │   ├── login_test.robot           # Web login test
    │   └── create_offer_test.robot    # Web offer creation test
    └── mobile/
        └── login_mobile_test.robot    # Mobile login test (Appium)
```

---

## Running Tests

### All web tests

```bash
robot robot-tests/tests/web
```

### All mobile tests

```bash
robot robot-tests/tests/mobile
```

### A single test file

```bash
robot robot-tests/tests/web/login_test.robot
```

### With a specific browser

```bash
robot --variable BROWSER:firefox robot-tests/tests/web
```

---

## Prerequisites

- Python 3.10+
- `pip install -r requirements.txt`
- Google Chrome + matching ChromeDriver on `$PATH` (web tests)
- Appium server running at `APPIUM_URL` (mobile tests)

---

## Adding New Tests

1. Add page locators / actions in `resources/pages/`.
2. Add reusable keywords in `resources/keywords/`.
3. Create new test files in `tests/web/` or `tests/mobile/`.
4. Import the relevant resource files at the top of your test.

---

## Reports

Robot Framework generates HTML reports automatically after each run:

```
output.xml
log.html
report.html
```

Open `report.html` in a browser to review results.
