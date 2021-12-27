from permissions import can_access
from db import Storage

def test_can_access__access_with_data_record(storage: Storage):
    assert can_access(user_id=4, product_id=2, storage=storage)

def test_can_access__cannot_access_with_data_record(storage: Storage):
    assert not can_access(user_id=4, product_id=1, storage=storage)

def test_can_access__cannot_access_without_record(storage: Storage):
    assert not can_access(user_id=1, product_id=2, storage=storage)
