import json
from pathlib import Path

import allure
import pytest

from TestData.random_data import unique_suffix
from Utils import apiutil, configparser, csv_util

DATA_DIR = Path(__file__).resolve().parent.parent / "TestData"


@allure.feature("Product Management")
class TestProductManagement:

    @pytest.mark.regression
    @pytest.mark.parametrize("i", range(2))
    @allure.title("Create product returns 200 and echoes the title")
    def test_create_product(self, login_details, i):
        with open(DATA_DIR / "create_product.json", encoding="utf-8") as f:
            payload = json.load(f)

        payload["title"] = f"QA Product {i} {unique_suffix()}"

        resp = apiutil.post_API_request(
            configparser.get_url('demo', 'create_product_url'),
            body=payload,
            op_headers=login_details["headers"],
        )

        assert resp.status_code in (200, 201), f"Unexpected status {resp.status_code}"
        body = resp.json()
        assert body["title"] == payload["title"]

        csv_util.save_record("product", body["id"], body["title"])
