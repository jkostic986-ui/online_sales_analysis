from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product: Product):
        self.cart_items.append(product)

    def calculate_total(self):
        total = sum(product.price for product in self.cart_items)
        return total
    
    def show_cart(self):
        print("Items in cart:")
        for product in self.cart_items:
            print(f"- {product.name}: ${product.price}")
        print(f"Total: ${self.calculate_total()}")
