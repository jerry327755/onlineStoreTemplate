class Cart:
    def __init__(self, product_list):
        self.product_list= product_list

    def __str__(self):
        return f" Products in cart: {self.product_list}"
        
