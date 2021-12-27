from datetime import datetime
from typing import Iterable
from models import User, ChargeableUser
from db import Storage


def should_charge(users: Iterable[User], storage: Storage, checkpoint: datetime) -> Iterable[ChargeableUser]:
    """Returns users that should be charged at the checkpoint time."""

    return []

def charge_subscriptions(users: Iterable[User], storage: Storage) -> None:
    """Charge users if possible. Otherwise revoke permissions"""
    pass

def revoke_access(user: User, product_id: int, storage: Storage) -> None:
    pass

def update_access(user: User, product_id: int, checkpoint: datetime) -> None:
    pass