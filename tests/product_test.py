def test_product_init(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


def test_new_product(add_product):
    assert add_product


def test_str(product_samsung):
    assert str(product_samsung) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'


def test_add(add_all):
    assert add_all == 180000.0


def test_smartphone_init(product_smartphone):
    assert product_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone.price == 180000.0
    assert product_smartphone.quantity == 5
    assert product_smartphone.efficiency == 95.5
    assert product_smartphone.model == "S23 Ultra"
    assert product_smartphone.memory == 256
    assert product_smartphone.color == "Серый"


def test_smartphone_add(add_smartphone):
    assert add_smartphone == 180000.0


def test_LawnGrass_init(product_LawnGrass):
    assert product_LawnGrass.name == "Газонная трава"
    assert product_LawnGrass.description == "Элитная трава для газона"
    assert product_LawnGrass.price == 500.0
    assert product_LawnGrass.quantity == 20
    assert product_LawnGrass.country == "Россия"
    assert product_LawnGrass.germination_period == "7 дней"
    assert product_LawnGrass.color == "Зеленый"
