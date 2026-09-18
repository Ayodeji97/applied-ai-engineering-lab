from unittest.mock import patch

from labs.workshop_order_cli.order import Number, format_order


def sample_order() -> dict[str, str | Number]:
    return {
        "customer_name": "Amaka",
        "garment": "Wedding gown",
        "price": 150_000,
        "deposit": 50_000,
        "status": "sewing",
    }


def test_formats_exact_order_summary() -> None:
    assert format_order(sample_order()) == (
        "Customer: Amaka\n"
        "Garment: Wedding gown\n"
        "Price: ₦150,000\n"
        "Deposit: ₦50,000\n"
        "Balance: ₦100,000\n"
        "Status: Sewing"
    )


def test_returns_a_string() -> None:
    assert isinstance(format_order(sample_order()), str)


def test_formats_currency_with_thousands_separators() -> None:
    order = sample_order()
    order.update(price=1_250_000, deposit=250_000)

    lines = format_order(order).splitlines()

    assert lines[2:5] == [
        "Price: ₦1,250,000",
        "Deposit: ₦250,000",
        "Balance: ₦1,000,000",
    ]


def test_balance_comes_from_price_minus_deposit() -> None:
    order = sample_order()
    order.update(price=80_000, deposit=30_000)
    assert "Balance: ₦50,000" in format_order(order).splitlines()

    order["deposit"] = 80_000
    assert "Balance: ₦0" in format_order(order).splitlines()


def test_uppercases_first_letter_of_status() -> None:
    order = sample_order()
    order["status"] = "ready for fitting"

    assert format_order(order).splitlines()[-1] == "Status: Ready for fitting"


def test_does_not_modify_input_mapping() -> None:
    order = sample_order()
    original = order.copy()

    format_order(order)

    assert order == original


def test_does_not_call_print() -> None:
    with patch("builtins.print") as print_mock:
        format_order(sample_order())

    print_mock.assert_not_called()


def test_normalizes_uppercase_status() -> None:
    order = sample_order()
    order["status"] = "READY"

    assert format_order(order).splitlines()[-1] == "Status: Ready"
