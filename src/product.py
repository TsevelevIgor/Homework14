class Product:
    """Класс товаров"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация товаров"""
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity
