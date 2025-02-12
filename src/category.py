class Category:
    """Класс категорий"""
    name: str
    description: str
    products: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Инициализация категорий"""
        self.name = name
        self.__products = products
        self.description = description
        Category.category_count += 1
        Category.product_count += 1

    def add_product(self, new_product):
        """Метод добавления нового товара"""
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для вывода списка товаров"""
        product_str = ""
        for product in self.__products:
            product_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return product_str

    def __str__(self):
        sum_product = 0
        for product in self.__products:
            sum_product += product.quantity
        return f'{self.name}, количество продуктов: {sum_product} шт.'
