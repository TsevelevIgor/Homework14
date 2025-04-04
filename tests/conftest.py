import pytest

from src.category import Category
from src.product import Product, Smartphone, LawnGrass


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


@pytest.fixture()
def add_all():
    return 180000.0


@pytest.fixture()
def product_smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                      "S23 Ultra", 256, "Серый")


@pytest.fixture()
def add_smartphone():
    return 180000.0


@pytest.fixture()
def product_LawnGrass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
