import pytest

from src.Product import Product
from src.Category import Category


@pytest.fixture()
def product_samsung():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_Productinit():
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.discripton == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


@pytest.fixture()
def category_smartphone():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только "
                    "коммуникации, но и получения дополнительных "
                    "функций для удобства жизни",
                    [product1, product2, product3])


def test_Categoryinit():
    assert category_smartphone.name == "Смартфоны"
    assert category_smartphone.discripton == ("Смартфоны, как средство не только "
                                              "коммуникации, но и получения дополнительных ")
    assert category_smartphone.products == [product1, product2, product3]
