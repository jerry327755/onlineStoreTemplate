from database.db import Database
class db_myTest:
    def test_product_categories(self):
        FRUITS = 'Fruit'
        VEGETABLES = 'Vegetables'
        SEEDS =  'Seeds'
        DIARY = 'Diary'
        db = Database('../database/store_records.db')
        db.get_item_category_by_id(1)
        elements=db.get_items_by_category(FRUITS)
        self.test_each_category(FRUITS, elements)
        elements = db.get_items_by_category(VEGETABLES)
        self.test_each_category(VEGETABLES, elements)
        elements = db.get_items_by_category(SEEDS)
        self.test_each_category(SEEDS, elements)
        elements = db.get_items_by_category(DIARY)
        self.test_each_category(DIARY, elements)

    def test_each_category(self, category, elements):
        for item in elements:
            if item['category'] != category:
                print("test_product_category test failed", category)
                return False
        print('test_product_category test passed',category)
        return True


my_test=db_myTest()
my_test.test_product_categories()
    
    
            


