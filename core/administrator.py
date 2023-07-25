class Administrator:
    def __init__(self, name, last_name, address, email, telephone_number):
        self.name=name
        self.last_name=last_name
        self.address=address
        self.email=email
        self.telephone_number=telephone_number

    def __str__(self):
        return f"Name: {self.name} Last Name: {self.last_name} Address: {self.address} Email: {self.email} Telephone Number: {self.telephone_number}"
        
