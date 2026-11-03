import json
from pathlib import Path

import allure
import pytest

from TestData.random_data import generate_user_details
from Utils import apiutil, configparser, csv_util

DATA_DIR = Path(__file__).resolve().parent.parent / "TestData"


@allure.feature("User Management")
class TestUserManagement:

    @pytest.mark.smoke
    @pytest.mark.parametrize("i", range(2))
    @allure.title("Create user returns 200 and echoes the username")
    def test_create_user(self, login_details, i):
        with open(DATA_DIR / "create_user.json", encoding="utf-8") as f:
            payload = json.load(f)

        username, email = generate_user_details()
        payload["firstName"] = f"QA{i}"
        payload["username"] = username
        payload["email"] = email

        resp = apiutil.post_API_request(
            configparser.get_url('demo', 'create_user_url'),
            body=payload,
            op_headers=login_details["headers"],
        )

        assert resp.status_code in (200, 201), f"Unexpected status {resp.status_code}"
        body = resp.json()
        assert body["username"] == username
        assert body["id"] is not None

        csv_util.save_record("user", body["id"], body["username"])
