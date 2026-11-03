# REST API Test Framework (pytest + requests + Allure)

API automation framework built with **Python, pytest, requests, and Allure**. It runs against [DummyJSON](https://dummyjson.com), a free open-source fake REST API, so anyone can run it without credentials or a private system.

## Tech Stack
- Python 3.10+
- pytest
- requests
- Allure reports (allure-pytest)

## Project Structure

```
api-automation-framework/
├── Config/config.ini                 Base URLs and endpoints (one section per environment)
├── Utils/
│   ├── apiutil.py                    GET / POST / PATCH / DELETE / multipart helpers
│   ├── configparser.py               Reads Config/config.ini (get_url(env, service))
│   ├── csv_util.py                   Records created IDs to reports/created_records.csv
│   └── login.py                      Logs in once per session, returns auth headers
├── TestData/
│   ├── random_data.py                Unique usernames and product titles
│   ├── create_user.json              User payload template
│   ├── create_product.json           Product payload template
│   └── logincreds.json               Public demo credentials for DummyJSON
├── TestModules/
│   ├── test_user_management.py       Create user tests
│   └── test_product_management.py    Create product tests
├── conftest.py                       Session fixture: login_details
├── pytest.ini                        Test path, markers, Allure output
├── requirements.txt
└── .gitignore
```

## Design Notes
- **Config-driven:** Every endpoint lives in `Config/config.ini`. Add an environment by adding a section.
- **One login per session:** The `login_details` fixture is session-scoped, so tests reuse the token.
- **No hard-coded data in tests:** Payloads come from `TestData/` and are made unique per run.
- **Records saved, secrets not:** Created IDs are logged to a git-ignored CSV. No passwords are stored.
- **SSL verification on:** requests verifies certificates by default. The demo site has a valid one.

## Setup

```bash
git clone https://github.com/<your-username>/api-automation-framework.git
cd api-automation-framework

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running Tests

```bash
pytest                            # run everything
pytest -m smoke                   # smoke tests only
pytest TestModules/test_user_management.py
```

### Allure Report

```bash
pytest                            # results go to reports/allure-results
allure serve reports/allure-results
```

Requires the [Allure CLI](https://allurereport.org/docs/install/).

## Test Coverage

| Module | Tests | What's covered |
|---|---|---|
| User management | 2 | Create user returns 200, username is echoed back |
| Product management | 2 | Create product returns 200, title is echoed back |

## Author
**Your Name** · [LinkedIn](https://linkedin.com/in/your-profile) · [Email](mailto:you@example.com)
