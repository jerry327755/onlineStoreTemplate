class Product:
    def __init__(self, name, category, price, cost, stock):
        self.name= name
        self.category=category
        self.price = price
        self.cost = cost
        self.stock=stock
    def __str__(self):
        return f"Name :{self.name} Category: {self.category} Price: {self.price} Cost: {self.cost} Stock: {self.stock}"

