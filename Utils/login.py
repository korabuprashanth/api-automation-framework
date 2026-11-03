import json
import os

from Utils import apiutil, configparser

base_path = os.path.dirname(os.path.dirname(__file__))
filename = os.path.join(base_path, "TestData", "logincreds.json")


def get_login_details():
    """Log in once and return the auth headers and IDs the tests need."""
    with open(filename, "r", encoding="utf-8") as f:
        payload = json.load(f)

    resp = apiutil.post_API_request(configparser.get_url('demo', 'login_url'), body=payload)
    resp.raise_for_status()
    data = resp.json()

    return {
        "headers": {"Authorization": "Bearer " + data["accessToken"]},
        "user_id": data["id"],
        "username": data["username"],
    }
