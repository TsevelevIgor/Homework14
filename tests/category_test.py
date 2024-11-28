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