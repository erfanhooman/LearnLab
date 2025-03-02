class Product:
    def __init__(self, name, barcode, prices=[]):
        self.name = name
        self.barcode = barcode
        self.prices = prices
        self.median_price = self.calculate_median()

    def calculate_median(self):
        n = len(self.prices)
        if n == 0:
            return 0
        sorted_prices = sorted(self.prices)
        if n % 2 == 1:
            return sorted_prices[n // 2]
        else:
            return (sorted_prices[n // 2 - 1] + sorted_prices[n // 2]) / 2

    def update_price(self, new_price):
        self.prices.append(new_price)
        self.median_price = self.calculate_median()

    def cheaper_than(self, price):
        return [barcode for barcode, product in store.items() if product.median_price < price]

    def more_expensive_than(self, price):
        return [barcode for barcode, product in store.items() if product.median_price > price]

    def in_price_range(self, min_price, max_price):
        return [barcode for barcode, product in store.items() if min_price <= product.median_price <= max_price]

    def __str__(self):
        return f"Name: {self.name}, Barcode: {self.barcode}, Median Price: {self.median_price}, Prices: {self.prices}"

store = {}

def add_product():
    name = input("Enter product name: ")
    barcode = input("Enter product barcode: ")
    
    if barcode in store:
        print("Product with this barcode already exists.")
        return
    
    prices = list(map(float, input("Enter prices (separated by commas): ").split(',')))
    store[barcode] = Product(name, barcode, prices)
    print(f"Product {name} added successfully.")

def update_price():
    barcode = input("Enter product barcode to update price: ")
    
    if barcode not in store:
        print("Product not found.")
        return
    
    new_price = float(input("Enter new price: "))
    store[barcode].update_price(new_price)
    print(f"Updated median price: {store[barcode].median_price}")

def remove_product():
    barcode = input("Enter product barcode to remove: ")
    
    if barcode not in store:
        print("Product not found.")
        return
    
    del store[barcode]
    print("Product removed successfully.")

def show_products():
    if not store:
        print("No products in the store.")
        return
    
    for product in store.values():
        print(product)

def find_cheaper():
    barcode = input("Enter barcode of the product: ")
    
    if barcode not in store:
        print("Product not found.")
        return
    
    price = store[barcode].median_price
    cheaper_barcodes = store[barcode].cheaper_than(price)
    print(f"Products cheaper than {price}: {cheaper_barcodes}")

def find_more_expensive():
    barcode = input("Enter barcode of the product: ")
    
    if barcode not in store:
        print("Product not found.")
        return
    
    price = store[barcode].median_price
    expensive_barcodes = store[barcode].more_expensive_than(price)
    print(f"Products more expensive than {price}: {expensive_barcodes}")

def find_in_price_range():
    min_price = float(input("Enter minimum price: "))
    max_price = float(input("Enter maximum price: "))
    
    products_in_range = []
    for barcode, product in store.items():
        if min_price <= product.median_price <= max_price:
            products_in_range.append(barcode)
    
    print(f"Products in the price range {min_price}-{max_price}: {products_in_range}")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Add product")
        print("2. Update price")
        print("3. Remove product")
        print("4. Show all products")
        print("5. Find cheaper products")
        print("6. Find more expensive products")
        print("7. Find products in a price range")
        print("8. Exit")
        
        choice = input("Enter choice (1-8): ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            update_price()
        elif choice == '3':
            remove_product()
        elif choice == '4':
            show_products()
        elif choice == '5':
            find_cheaper()
        elif choice == '6':
            find_more_expensive()
        elif choice == '7':
            find_in_price_range()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
