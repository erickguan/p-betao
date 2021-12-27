from datetime import datetime, timedelta, timezone
from models import Product, User, UserAccess, Transaction

MOCK_PRODUCTS = [
    Product(1, "Product A", 5900, 2900),
    Product(2, "Product B", 10900, 1090)
]

MOCK_USERS = [
    User(1, "bob@betao.se", True),
    User(2, "john@betao.se", True),
    User(3, "peter@betao.se", True),
    User(4, "andrew@betao.se", True),
    User(5, "boris@betao.se", True),
]

MOCK_TRANSACTIONS = [
    Transaction(1, user_id=1, product_id=1, date=datetime(2021, 1, 1, tzinfo=timezone.utc), price=2900),
    Transaction(2, user_id=2, product_id=1, date=datetime(2021, 1, 15, tzinfo=timezone.utc), price=2900),
    Transaction(3, user_id=3, product_id=2, date=datetime(2021, 1, 15, tzinfo=timezone.utc), price=1090),
    Transaction(4, user_id=4, product_id=2, date=datetime(2021, 1, 17, tzinfo=timezone.utc), price=1090),
    Transaction(5, user_id=5, product_id=1, date=datetime(2020, 12, 15, tzinfo=timezone.utc), price=2900),
    Transaction(6, user_id=5, product_id=2, date=datetime(2020, 12, 15, tzinfo=timezone.utc), price=1090),
]

CURRENT_DATE = datetime(2021, 2, 16, tzinfo=timezone.utc)

class Storage:
    """Data storage in memory"""

    def __init__(self):
        self.products = {
            product.name: product for product in MOCK_PRODUCTS
        }

        self.users = {
            user.email: user for user in MOCK_USERS
        }

        self.transactions = {
            transaction.id: transaction for transaction in MOCK_TRANSACTIONS
        }

        self.user_access = {
            idx+1: UserAccess(idx+1, txn.user_id, txn.product_id, txn.date + timedelta(days=30) >= CURRENT_DATE) for idx, txn in enumerate(MOCK_TRANSACTIONS)
        }
