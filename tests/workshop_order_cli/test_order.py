from typing import Any, cast

import pytest

pytest = cast(Any, pytest)

from labs.workshop_order_cli.order import calculate_balance


def test_calculates_outstanding_balance() -> None:
    order = {"price": 150_000, "deposit": 50_000}

    assert calculate_balance(order) == 100_000


def test_allows_fully_paid_order() -> None:
    order = {"price": 80_000, "deposit": 80_000}

    assert calculate_balance(order) == 0


@pytest.mark.parametrize(
    ("order", "message"),
    [
        ({"deposit": 10_000}, "price"),
        ({"price": 20_000}, "deposit"),
        ({"price": -20_000, "deposit": 0}, "negative"),
        ({"price": 20_000, "deposit": -1}, "negative"),
        ({"price": 20_000, "deposit": 30_000}, "greater"),
        ({"price": "many", "deposit": 0}, "number"),
    ],
)
def test_rejects_invalid_order(order: dict[str, object], message: str) -> None:
    with pytest.raises(ValueError, match=message):
        calculate_balance(order)  # type: ignore[arg-type]


def test_does_not_modify_order() -> None:
    order = {"price": 50_000, "deposit": 10_000}
    original = order.copy()

    calculate_balance(order)

    assert order == original
