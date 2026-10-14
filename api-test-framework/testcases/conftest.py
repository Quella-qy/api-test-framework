import pytest
from api.base_request import BaseRequest

@pytest.fixture(scope="session")
def api():
    return BaseRequest()