import json
import os

class Inventory:
    def __init__(self, data_file='data/products.json'):
        self.data_file = data_file
        self.products = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                try:
                    self.products = json.load(f)
                except json.JSONDecodeError:
                    self.products = []
        else:
            # Ensure directory exists
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            with open(self.data_file, 'w') as f:
                json.dump([], f)

    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.products, f, indent=4)

    def add_product(self, name, category, quantity, cost, sale_price):
        product = {
            'name': name,
            'category': category,
            'quantity': quantity,
            'cost': cost,
            'sale_price': sale_price
        }
        self.products.append(product)
        self.save_data()
        print(f"Product '{name}' added successfully.")

    def list_products(self):
        if not self.products:
            print("No products in inventory.")
            return
        for product in self.products:
            print(f"{product['name']} ({product['category']}): {product['quantity']} units. Cost: {product['cost']}, Sale Price: {product['sale_price']}")

    def search_product(self, name):
        found = False
        for product in self.products:
            if product['name'].lower() == name.lower():
                print(f"Found product: {product}")
                found = True
        if not found:
            print("Product not found.")

    def add_stock(self, name, quantity):
        for product in self.products:
            if product['name'].lower() == name.lower():
                product['quantity'] += quantity
                self.save_data()
                print(f"Added {quantity} units to {name}.")
                return
        print("Product not found.")

    def register_output(self, name, quantity):
        for product in self.products:
            if product['name'].lower() == name.lower():
                if product['quantity'] >= quantity:
                    product['quantity'] -= quantity
                    self.save_data()
                    print(f"Removed {quantity} units from {name}.")
                else:
                    print(f"Not enough stock to remove {quantity} units.")
                return
        print("Product not found.")

    def calculate_profit_margin(self, name):
        for product in self.products:
            if product['name'].lower() == name.lower():
                cost = product['cost']
                sale_price = product['sale_price']
                if cost == 0:
                    print("Cost is zero, cannot calculate margin.")
                else:
                    margin = ((sale_price - cost) / cost) * 100
                    print(f"Profit margin for {name}: {margin:.2f}%")
                return
        print("Product not found.")
