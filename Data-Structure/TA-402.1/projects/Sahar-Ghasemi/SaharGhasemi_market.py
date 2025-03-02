# market project "Sahar Ghasemi"

from os import system

class Product:
    def __init__(self, name, product_id, price):
        self.name = name
        self.product_id = product_id
        self.current_price = price
        self.price_count = 0
        self.previous_prices = [price]
        self.median_price = price
        self.left = None
        self.right = None

class ProductBST:
    def __init__(self):
        self.root = None

    def add_product(self, name, product_id, price):
        if self.find_product(self.root, product_id) is not None:
            print("Product with this ID already exists.")
            return
        self.root = self._add_product(self.root, name, product_id, price)

    def _add_product(self, node, name, product_id, price):
        if node is None:
            return Product(name, product_id, price)
        if price < node.current_price:
            node.left = self._add_product(node.left, name, product_id, price)
        else:
            node.right = self._add_product(node.right, name, product_id, price)
        return node

    def change_price(self, product_id, new_price):
        product = self.find_product(self.root, product_id)
        if product:
            product.current_price = new_price
            product.previous_prices.append(product.current_price)
            product.median_price = self.calculate_median(product.previous_prices)

    def find_product(self, node, product_id):
        if node is None:
            return None
        if node.product_id == product_id:
            return node
        if product_id < node.product_id:
            return self.find_product(node.left, product_id)
        return self.find_product(node.right, product_id)

    def calculate_median(self, prices):
        prices.sort()
        n = len(prices)
        if n % 2 == 0:
            return (prices[n // 2 - 1] + prices[n // 2]) / 2
        return prices[n // 2]

    def delete_product(self, product_id):
        self.root = self._delete_product(self.root, product_id)

    def _delete_product(self, node, product_id):
        if node is None:
            return node
        if product_id < node.product_id:
            node.left = self._delete_product(node.left, product_id)
        elif product_id > node.product_id:
            node.right = self._delete_product(node.right, product_id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._find_min(node.right)
            node.product_id = min_larger_node.product_id
            node.current_price = min_larger_node.current_price
            node.previous_prices = min_larger_node.previous_prices
            node.median_price = min_larger_node.median_price
            node.right = self._delete_product(node.right, min_larger_node.product_id)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def find_median_price(self, product_id):
        product = self.find_product(self.root, product_id)
        return product.median_price if product else None

    def find_expensive_products(self, price):
        return self._find_expensive_products(self.root, price)

    def _find_expensive_products(self, node, price):
        if node is None:
            return []
        result = []
        if node.current_price > price:
            result.append(node)
        result.extend(self._find_expensive_products(node.left, price))
        result.extend(self._find_expensive_products(node.right, price))
        return result
    
    def find_cheaper_products(self, price):
        return self._find_cheaper_products(self.root, price)

    def _find_cheaper_products(self, node, price):
        if node is None:
            return []
        result = []
        if node.current_price < price:
            result.append(node)
        result.extend(self._find_cheaper_products(node.left, price))
        result.extend(self._find_cheaper_products(node.right, price))
        return result
    
    def find_products_in_range(self, low, high):
        return self._find_products_in_range(self.root, low, high)

    def _find_products_in_range(self, node, low, high):
        if node is None:
            return []
        result = []
        if low <= node.current_price <= high:
            result.append(node)
        result.extend(self._find_products_in_range(node.left, low, high))
        result.extend(self._find_products_in_range(node.right, low, high))
        return result

bst = ProductBST()
while True:
    print("\n1: Add a new product")
    print("2: Change a product price")
    print("3: Find the median price of a product by ID")
    print("4: Delete a product")
    print("5: Find products more expensive than a specific price")
    print("6: Find products cheaper than a specific price")  
    print("7: Show products in a particular price range")
    print("8: Exit")
    choice = input("Choose an option: ")
        
    if choice == '1':
        name = input("Enter product name: ")
        product_id = input("Enter product ID: ")
        price = float(input("Enter product price: "))
        bst.add_product(name, product_id, price)
    elif choice == '2':
        product_id = input("Enter product ID: ")
        new_price = float(input("Enter new price: "))
        bst.change_price(product_id, new_price)
    elif choice == '3':
        product_id = input("Enter product ID: ")
        median_price = bst.find_median_price(product_id)
        print(f"Median price: {median_price}")
    elif choice == '4':
        product_id = input("Enter product ID: ")
        bst.delete_product(product_id)
    elif choice == '5':
        price = float(input("Enter price: "))
        expensive_products = bst.find_expensive_products(price)
        for product in expensive_products:
            print(f"Product ID: {product.product_id}, Name: {product.name}, Current Price: {product.current_price}")
    elif choice == '6': 
        price = float(input("Enter price: "))
        cheaper_products = bst.find_cheaper_products(price)
        for product in cheaper_products:
            print(f"Product ID: {product.product_id}, Name: {product.name}, Current Price: {product.current_price}")
    elif choice == '7':
        low = float(input("Enter low price: "))
        high = float(input("Enter high price: "))
        products_in_range = bst.find_products_in_range(low, high)
        for product in products_in_range:
            print(f"Product ID: {product.product_id}, Name: {product.name}, Current Price: {product.current_price}")
    elif choice == '8':
        break
    else:
        print("Invalid option. Please try again.")
    input("Enter a key to continue!  ")
    system("clear")
