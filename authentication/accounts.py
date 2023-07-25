

class Account:
    """
    Class to represent a user's account.
    Responsible for handling authentication for that user and storing 
    persistent data, such as user preferences/cart.

    """

    def __init__(self, name):
        pass
    
    def get_permission_level() -> int:
        pass

    def check_password(hash: str) -> bool:
        pass
    

class CustomerAccount(Account):
    
    def __init__(self, name):
        super().__init__(name)

    # Customers have the lowest permission level
    def get_permission_level() -> int:
        return 1

class ManagerAccount(Account):
    
    def __init__(self, name):
        super().__init__(name)

    # Managers have the second lowest
    def get_permission_level() -> int:
        return 2

class AdminAccount(Account):
    
    def __init__(self, name):
        super().__init__(name)

    # and site admin has the highest
    def get_permission_level() -> int:
        return 3


