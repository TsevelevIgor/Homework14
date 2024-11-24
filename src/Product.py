class Product:
    name: str
    description: str
    price: str
    quantity: str

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity