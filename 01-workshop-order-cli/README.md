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

## Coming checkpoints

- 1.2 Format one Order for display
- 1.3 Work with a list of Orders
- 1.4 Filter by status and calculate totals
- 1.5 Validate Customer and Order input
- 1.6 Replace dictionaries with typed models
- 1.7 Save and load JSON
- 1.8 Refactor into modules and repositories
- 1.9 Phase assessment using a fresh domain task

