"""Unique test data. example.com addresses are reserved for documentation."""
import uuid


def unique_suffix():
    return uuid.uuid4().hex[:8]


def generate_user_details():
    username = f"qa_user_{unique_suffix()}"
    email = f"{username}@example.com"
    return username, email
