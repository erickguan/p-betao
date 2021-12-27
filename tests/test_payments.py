from db import Storage
from models import Transaction
from payments import revoke_access, should_charge, update_access
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


def test_update_access__creates_record_at_last_day(storage: Storage):
    storage.transactions.update({
        7: Transaction(7,  user_id=3, product_id=1, date=datetime(2021, 1, 17, tzinfo=timezone.utc), price=2900)
    })
    update_access(storage.users["peter@betao.se"], 7, storage)

    assert storage.user_access["3__1"].has_access


def test_should_charge__does_not_charge_within_30_days(storage: Storage):
    charged = list(should_charge([storage.users["bob@betao.se"]], storage, datetime(2021, 1, 30, tzinfo=timezone.utc)))

    assert len(charged) == 0

def test_should_charge__charge_when_more_than_30_days(storage: Storage):
    charged = list(should_charge([storage.users["bob@betao.se"]], storage, datetime(2021, 1, 31, tzinfo=timezone.utc)))

    assert len(charged) == 1
    assert charged[0].id == 1
    assert charged[0].product_id == 1
 
def test_should_charge__charge_two_products(storage: Storage):
    charged = list(should_charge([storage.users["boris@betao.se"]], storage, datetime(2021, 1, 14, tzinfo=timezone.utc)))

    assert len(charged) == 2
    assert charged[0].id == 5
    assert charged[0].product_id == 1

    assert charged[1].id == 5
    assert charged[1].product_id == 2
