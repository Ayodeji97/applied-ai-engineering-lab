from collections.abc import Mapping

type Number = int | float
type Order = Mapping[str, str | Number]


def calculate_balance(order: Order) -> Number:
    """Return the unpaid balance for an Order.

    Raises:
        ValueError: If price or deposit is missing, non-numeric, negative, or inconsistent.
    """
    for field in ("price", "deposit"):
        if field not in order:
            raise ValueError(f"Missing {field}")

    price = order["price"]
    deposit = order["deposit"]
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise ValueError("price must be a number")
    if isinstance(deposit, bool) or not isinstance(deposit, (int, float)):
        raise ValueError("deposit must be a number")
    if price < 0 or deposit < 0:
        raise ValueError("price and deposit must not be negative")
    if deposit > price:
        raise ValueError("deposit must not be greater than price")

    return price - deposit
