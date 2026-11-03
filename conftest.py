import pytest

from Utils.login import get_login_details


@pytest.fixture(scope="session")
def login_details():
    """Log in once for the whole test session."""
    return get_login_details()
