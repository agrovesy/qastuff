

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def total_value(self):
        return self.price * self.quantity
    
    def add_stock(self, quantity):
        self.quantity += quantity
        
    def remove_item(self, quantity):
        if quantity > self.quantity:
            print("not enough stock")
        else:
            self.quantity -= quantity
            
    def __str__(self):
        return f"{self.name} {self.price} {self.quantity}"
    
    
prod = Product("macbook pro", 10001, 5)

print(prod.total_value())
prod.add_stock(5)
print(prod.quantity)

prod.remove_item(9)
print(prod.quantity)
prod.remove_item(1000000)
print(prod)
        



