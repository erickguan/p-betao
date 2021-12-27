from db import Storage
from models import Transaction
from payments import revoke_access, update_access
from datetime import datetime, timedelta, timezone

def test_revoke_access__revokes(storage: Storage):
    revoke_access(storage.users["andrew@betao.se"], 2, storage) # user_id=4
    
    assert not storage.user_access["4__2"].has_access


def test_revoke_access__revokes_when_no_record(storage: Storage):
    revoke_access(storage.users["bob@betao.se"], 2, storage) # user_id=1

    assert not storage.user_access["1__2"].has_access

def test_update_access__update_access(storage: Storage):
    storage.transactions.update({
        7: Transaction(7,  user_id=1, product_id=1, date=datetime(2021, 2, 16, tzinfo=timezone.utc), price=2900)
    })
    update_access(storage.users["bob@betao.se"], 7, storage)

    assert storage.user_access["1__1"].has_access


def test_update_access__creates_record(storage: Storage):
    storage.transactions.update({
        7: Transaction(7,  user_id=1, product_id=2, date=datetime(2021, 2, 16, tzinfo=timezone.utc), price=2900)
    })
    update_access(storage.users["bob@betao.se"], 7, storage)

    assert storage.user_access["1__2"].has_access