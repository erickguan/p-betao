from db import Storage
import pytest

@pytest.fixture(name="storage")
def make_storage() -> Storage:
    return Storage()
