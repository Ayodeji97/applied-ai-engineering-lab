from labs.workshop_order_cli.order import calculate_balance


def main() -> None:
    order = {
        "customer_name": "Amaka",
        "garment": "Wedding gown",
        "price": 150_000,
        "deposit": 50_000,
        "status": "sewing",
    }

    balance = calculate_balance(order)
    print(f"Customer: {order['customer_name']}")
    print(f"Order: {order['garment']}")
    print(f"Balance: ₦{balance:,.0f}")


if __name__ == "__main__":
    main()

