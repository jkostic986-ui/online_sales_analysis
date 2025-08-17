from product import Product
from product_manager import ProductManager

manager = ProductManager()


manager.add_product(Product("Telefon", 40000, 5))
manager.add_product(Product("Laptop", 80000, 3))
manager.add_product(Product("Miš", 1500, 10))


manager.display_all_products()
print(f"Ukupna vrednost: {manager.total_inventory_value()} RSD")

