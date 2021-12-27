from datetime import datetime, timedelta
from typing import Iterable
from models import User, ChargeableUser, UserAccess
from db import Storage, CURRENT_DATE
import random


def should_charge(users: Iterable[User], storage: Storage, checkpoint: datetime) -> Iterable[ChargeableUser]:
    """Returns users that should be charged at the checkpoint time."""

    for user in users:
        transactions = [txn for txn in storage.transactions.values() if txn.user_id == user.id]
        for txn in transactions:
            if txn.date + timedelta(days=30) <= checkpoint:
                yield ChargeableUser(user.id, user.email, user.has_access, txn.product_id)


def charge_subscriptions(users: Iterable[User], storage: Storage) -> None:
    """Charge users if possible. Otherwise revoke permissions"""

    for user in should_charge(users, storage, CURRENT_DATE):
        success = random.choice([True, False])
        if success:
            # update_access(user, <a transaction id>)
            pass
        else:
            # revoke_access(user, <a product id>)
            pass

def revoke_access(user: User, product_id: int, storage: Storage) -> None:
    if product_id <= 0: return

    access_key = f"{user.id}__{product_id}"
    access = storage.user_access.get(access_key)
    if access:
        access.has_access = False
    else:
        storage.user_access.update({
            access_key: UserAccess(max([ua.id for ua in storage.user_access.values()])+1, user.id, product_id, False)
        })

def update_access(user: User, transaction_id: int, storage: Storage) -> None:
    if transaction_id <= 0: return
    txn = storage.transactions.get(transaction_id)
    if txn is None or txn.date + timedelta(days=30) < CURRENT_DATE:
        return

    access_key = f"{user.id}__{txn.product_id}"
    access = storage.user_access.get(access_key)
    if access:
        access.has_access = True
    else:
        storage.user_access.update({
            access_key: UserAccess(max([ua.id for ua in storage.user_access.values()])+1, user.id, txn.product_id, True)
        })
