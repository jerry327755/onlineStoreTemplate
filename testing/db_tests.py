from database.db import Database
from core.utils import dict_factory


def test_init_db(db: Database = None) -> tuple:
    """
    Tests that the database is initialized correctly.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/store_records.db") if db is None else db

    if db.database_path != "database/store_records.db":
        error = f"Error in test_init_db: Database path is not correct.\n  - Actual: {db.database_path}"
        return False, error
    else:
        return True, "Database path is correct."


def test_get_inventory_exists(db: Database = None) -> tuple:
    """
    Tests that the inventory is not empty.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/store_records.db") if db is None else db
    full_inventory = db.get_full_inventory()

    if len(full_inventory) == 0:
        error = f"Error in test_get_full_inventory: Full inventory is empty.\n  - Actual: {len(full_inventory)}"
        return False, error
    else:
        return True, "Full inventory is not empty."


def test_dict_factory_link(db: Database = None) -> tuple:
    """
    Tests that the row factory is linked to dict_factory.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """
    db = Database("database/store_records.db") if db is None else db
    row_factory = db.connection.row_factory

    if row_factory != dict_factory:
        error = f"Error in test_dict_factory_link: Row factory is not linked to dict_factory.\n  - Expected: {dict_factory}\n  - Actual: {row_factory}"
        return False, error
    else:
        return True, "Row factory is linked to dict_factory."


def test_check_connection_threaded(db: Database = None) -> tuple:
    """
    Tests that the database connection is not single threaded.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """

    db = Database("database/store_records.db") if db is None else db
    connection_is_threaded = db.connection.isolation_level is None

    if connection_is_threaded:
        error = f"Error in test_check_connection_single_thread: Connection is single threaded.\n  - Actual: {connection_is_threaded}"
        return False, error
    else:
        return True, "Connection is not single threaded."


def test_stock_filtered(db: Database = None) -> tuple:
    """
    Tests that the stock has been filtered from low-to-high and high-to-low.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """
    db = Database("database/store_records.db") if db is None else db

    products = db.get_full_inventory()
    low_to_high = sorted(products, key=lambda x: x['price'])
    high_to_low = sorted(products, key=lambda x: x['price'], reverse=True)

    for i in range(len(low_to_high) - 1):
        if low_to_high[i]['price'] > low_to_high[i + 1]['price']:
            error = f"Error in test_stock_filtered: Low_to_high stock is not filtered.\n  - Actual: False"
            return False, error

    for i in range(len(high_to_low) - 1):
        if high_to_low[i]['price'] < high_to_low[i + 1]['price']:
            error = f"Error in test_stock_filtered: High_to_low stock is not filtered.\n  - Actual: False"
            return False, error

    return True, "Stock is filtered successfully."


"""
This test ensures that each product is obtained based on its product category using a database.

"""




def test_product_category():
    """
    Retrieves products based on their categories from the database.

    Retrieves items for each category and performs individual category tests.

    Returns:
        bool: True if all tests passed, False is tests failed.
    """
    db = Database('database/store_records.db')

    def test_each_category(category, elements):
        """
        This test method verifies if the items in a category have the correct category.

        Args:
            category (STR): The category that each element should be in.
            elements (LIST): Product List

        Returns:
            bool: True if all items in the category have the correct category, False if products do not have the correct category.
        """
        for item in elements:
            if item['category'] != category:
                print("test_product_category test failed for category:", category)
                return False
        print('test_product_category test passed for category:', category)
        return True

    #Product categories
    FRUITS = 'Fruit'
    VEGETABLES = 'Vegetables'
    SEEDS = 'Seeds'
    DIARY = 'Diary'
    # Test Fruits category
    elements = db.get_items_by_category(FRUITS)
    if not test_each_category(FRUITS, elements):
        return False, "All tests failed"

    # Test Vegetables category
    elements = db.get_items_by_category(VEGETABLES)
    if not test_each_category(VEGETABLES, elements):
        return False, "All tests failed"

    # Test Seeds category
    elements = db.get_items_by_category(SEEDS)
    if not test_each_category(SEEDS, elements):
        return False, "All tests failed"

    # Test Dairy category
    elements = db.get_items_by_category(DIARY)
    if not test_each_category(DIARY, elements):
        return False, "All tests failed"

    return True, "All tests Passed"


