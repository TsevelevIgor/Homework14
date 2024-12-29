class Product:
    """Класс товаров"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация товаров"""
        self.name = name
        self.__price = price
        self.description = description
        self.quantity = quantity

    @classmethod
    def new_product(cls, products_dict):
        name = products_dict['name']
        description = products_dict['description']
        price = products_dict['price']
        quantity = products_dict['quantity']
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError('Цена не должна быть нулевая или отрицательная')
