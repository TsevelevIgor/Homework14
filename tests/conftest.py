import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def category_smartphone():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только " "коммуникации, но и получения дополнительных "
                    "функций для удобства жизни",
                    ["Samsung Galaxy S23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"])


@pytest.fixture()
def product_samsung():
    return Product("Samsung Galaxy S23 Ultra", "256GB, "
                                               "Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def add_product():
    return Product(
        name='Honor',
        description='512GB, зелёный цвет, 50MP камера',
        price=37000.0,
        quantity=3
    )
