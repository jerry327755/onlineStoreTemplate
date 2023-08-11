import sqlite3
import uuid


def dict_factory(cursor: sqlite3.Cursor, row: tuple) -> dict:
    """
    Creates a dictionary from a row in the database. This is used to convert the rows into dictionaries.

    args:
        - cursor: The cursor of the database, which is a built-in sqlite3 class.
        - row: The row to convert into a dictionary.

    returns:
        - The dictionary of the row.
    """

    row_dict = {}
    for index, column in enumerate(cursor.description):
        row_dict[column[0]] = row[index]
    return row_dict


def calculate_cost(price: int, quantity: int, discount: float = 0.0, tax_rate: float = 0.05) -> list:
    """
    Calculates the cost of an item.

    args:
        - price: The price of the item.
        - quantity: The quantity of the item.
        - discount: The discount of the item.
        - tax_rate: The tax rate of the item.

    returns:
        - The cost of the item as a float.
    """
    return [(price * quantity) * (1 - discount) * (tax_rate), (price * quantity) * (1 - discount)]


def calculate_total_cost(items: dict) -> list:
    """
    Calculates the total cost of a set of items.

    args:
        - items: A dictionary of items to calculate the total cost of.

    returns:
        - The total cost of the sale as a float.
    """
    subtotal = 0
    tax = 0
    for i in items:
        item = items[i]
        totals = calculate_cost(float(item["price"]), int(item["quantity"]),
                                     float(item["discount"]), float(item["tax_rate"]))
        tax += totals[0]
        subtotal += totals[1]
    return [subtotal, tax, subtotal + tax]


def generate_unique_id() -> str:
    """
    Generates a unique ID.

    args:
        - None

    returns:
        - A unique ID as a string.
    """
    return str(uuid.uuid4())
