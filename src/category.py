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
        self.products = products
        self.description = description
        Category.category_count += 1
        Category.product_count += 1
