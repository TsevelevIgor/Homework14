from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass


class MixinProduct:
    def __repr__(self):
        return f"{self.__class__.__name__}"


class Product(BaseProduct, MixinProduct):
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
        if self.quantity == 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')

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

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Подкласс Смартфоны"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is self.__class__:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError


class LawnGrass(Product):
    """Подкласс Трава газонная"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
