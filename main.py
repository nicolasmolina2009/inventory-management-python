from inventory import Inventory

def main():
    inv = Inventory()
    while True:
        print("\nInventory Management System")
        print("1. Add product")
        print("2. List products")
        print("3. Search product")
        print("4. Add stock entry")
        print("5. Register stock output")
        print("6. Calculate profit margin")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Product name: ")
            category = input("Category: ")
            quantity = int(input("Quantity: "))
            cost = float(input("Cost: "))
            sale_price = float(input("Sale price: "))
            inv.add_product(name, category, quantity, cost, sale_price)
        elif choice == '2':
            inv.list_products()
        elif choice == '3':
            name = input("Product name to search: ")
            inv.search_product(name)
        elif choice == '4':
            name = input("Product name: ")
            qty = int(input("Quantity to add: "))
            inv.add_stock(name, qty)
        elif choice == '5':
            name = input("Product name: ")
            qty = int(input("Quantity to remove: "))
            inv.register_output(name, qty)
        elif choice == '6':
            name = input("Product name: ")
            inv.calculate_profit_margin(name)
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
