class Order:
    def __init__(self, product_list, id, customer):
        self.product_list = product_list
        self.id = id
        self.customer = customer

    def __str__(self):
        return f"Id: {self.id} Product List {self.product_list} Customer {self.customer}"
 