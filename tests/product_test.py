def test_product_init(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


def test_new_product(add_product):
    assert add_product


def test_str(str_info):
    assert str_info


def test_add(add_info):
    assert add_info
