from product import Product
from product_manager import ProductManager

manager = ProductManager()


manager.add_product(Product("Telefon", 40000, 5))
manager.add_product(Product("Laptop", 80000, 3))
manager.add_product(Product("Miš", 1500, 10))


manager.display_all_products()
print(f"Ukupna vrednost: {manager.total_inventory_value()} RSD")


from cart import Cart



cart = Cart()
cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])

cart.show_cart()
print(f"Ukupna vrednost korpe: {cart.total_cart_value()} RSD")