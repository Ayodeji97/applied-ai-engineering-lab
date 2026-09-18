# Lab 01: Workshop Order CLI

## Purpose

Learn production Python by building a useful command-line tool for a fashion Workshop.

## Checkpoint 1.1: Calculate an Order balance

Given an Order dictionary containing `price` and `deposit`, return:

```text
price - deposit
```

### Rules

- `price` and `deposit` must be numbers.
- They must not be negative.
- `deposit` must not be greater than `price`.
- Invalid input must raise `ValueError` with a useful message.
- Do not change the input dictionary.

### Concepts introduced only as needed

- dictionaries and key lookup;
- functions and return values;
- `int` and `float`;
- conditions and Boolean expressions;
- exceptions;
- type hints;
- pytest assertions.

## Learning sequence

1. Read `src/labs/workshop_order_cli/order.py`.
2. Before coding, write down what each supplied test expects.
3. Run `uv run pytest tests/workshop_order_cli/test_order.py -v`.
4. Implement only `calculate_balance`.
5. Run the tests again.
6. Run `uv run ruff check .` and `uv run pyright`.
7. Complete the submission questions below.

## Submission

Return:

- your implementation or Git commit;
- complete test output;
- answers to these questions:
  1. Why is a dictionary appropriate for the first version?
  2. What can fail when accessing `order["price"]`?
  3. Why must we reject a deposit greater than the price?
  4. Did your function mutate the dictionary? How do you know?
  5. What help did you receive from a coding agent?

## Checkpoint 1.2: Format one Order for display

Implement `format_order(order: Order) -> str` in
`src/labs/workshop_order_cli/order.py`. The supplied stub deliberately raises
`NotImplementedError`; the formatter implementation is your exercise.

The input mapping contains `customer_name`, `garment`, `price`, `deposit`, and
`status`. For this checkpoint, assume all five fields are present, the text fields
are non-empty strings, and amounts are valid whole-naira integers following the
Checkpoint 1.1 rules. Fractional currency and additional validation are outside
this checkpoint.

For `customer_name="Amaka"`, `garment="Wedding gown"`, `price=150_000`,
`deposit=50_000`, and `status="sewing"`, return exactly:

```text
Customer: Amaka
Garment: Wedding gown
Price: ₦150,000
Deposit: ₦50,000
Balance: ₦100,000
Status: Sewing
```

### Rules

- Return a string with these six labels in this order, separated by newlines.
- Do not include a leading or trailing newline or extra spaces.
- Prefix each amount with `₦` and use comma thousands separators, without decimals.
- Calculate the balance as price minus deposit; a fully paid order has `Balance: ₦0`.
- Display the status with an uppercase first letter. For example,
  `ready for fitting` becomes `Ready for fitting`.
- Preserve the customer name and garment text.
- Do not modify the input mapping.
- Return the text; do not call `print`.

### Learning sequence

1. Explain the expected output and what each test checks in your own words.
2. Run `uv run pytest tests/workshop_order_cli/test_format_order.py -v`.
   All seven tests should initially fail with `NotImplementedError`.
3. Write your implementation of `format_order`.
4. Run the focused tests again, then `uv run pytest` once they pass.
5. Run `uv run ruff check .` and `uv run pyright`.
6. Explain how your code formats currency, calculates the balance, and avoids
   changing the input. Record what assistance you received.

The checkpoint stub, tests, and requirements were prepared with coding-agent
assistance. The formatter solution is left for Daniel to write.

## Coming checkpoints

- 1.3 Work with a list of Orders
- 1.4 Filter by status and calculate totals
- 1.5 Validate Customer and Order input
- 1.6 Replace dictionaries with typed models
- 1.7 Save and load JSON
- 1.8 Refactor into modules and repositories
- 1.9 Phase assessment using a fresh domain task
