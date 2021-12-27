from db import Storage


def can_access(user_id: int, product_id: int, storage: Storage) -> bool:
    if user_id <= 0: return False
    if product_id <= 0: return False

    record = storage.user_access.get(f"{user_id}__{product_id}")
    if record:
        return record.has_access
    return False
