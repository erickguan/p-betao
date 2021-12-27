from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int
    email: str
    has_access: bool

@dataclass
class Product:
    id: int
    name: str
    initial_price: int
    recurring_price: int

@dataclass
class Transaction:
    """Transaction data model.

    Args:
        user_id: Buyer's ID.
        product_id: Product paid for
        date: Purchase date
        price: actual price paid
    """

    id: int
    user_id: int
    product_id: int
    date: datetime
    price: int

@dataclass
class ChargeableUser(User):
    product_id: int

@dataclass
class UserAccess:
    id: int
    user_id: int
    product_id: int
    has_access: bool
