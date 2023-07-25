class User:
    def __init__(self, email, password, permissions):
        self.email=email
        self.password=password
        self.permissions=permissions
    def __str__(self):
        return f"Email: {self.email} Password: ******* Permissions {self.permissions}"

