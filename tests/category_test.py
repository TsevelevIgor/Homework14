from src.category import Category


def test_category_init(category_smartphone):
    assert category_smartphone.name == "Смартфоны"
    assert category_smartphone.description == ("Смартфоны, как средство не только "
                                               "коммуникации, но и получения дополнительных "
                                               "функций для удобства жизни")
    assert category_smartphone.products == ["Samsung Galaxy S23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"]


def count_test():
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_add_product(add_product):
    category_test = Category(
        name="Смартфоны",
        description=("Смартфоны, как средство не только "
                     "коммуникации, но и получения дополнительных "
                     "функций для удобства жизни"),
        products=[]
    )
    product_test = add_product

    category_test.add_product(product_test)
    assert category_test.product_count == 3


def test_str(category_smartphone):
    assert str(category_smartphone) == 'Смартфоны, количество продуктов: 27 шт.'


def test_middle_price():
    category_empty = Category("Смартфоны", "Категория смартфонов", [])
    category1 = Category("Смартфоны", "Категория смартфонов",
                         ["Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5,
                          "Iphone 15", "512GB, Gray space", 210000.0, 8,
                          "Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14])
    assert category_empty.middle_price() == 0
    assert category1.middle_price() == 140333.33
