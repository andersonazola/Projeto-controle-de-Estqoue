
invetory = []

class InvetoryControl:
    
    def register_product(self, name, quantity, price ):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.name = input("Product name: ")
        self.quantity = int(input("Quantities: "))
        self.price = float(input("Price: "))
        invetory.append({"name": name,"quantity": quantity, "price": price})
    
    def product_entry(self, name, quantity, price):
        if name in invetory:
            self.name = input("Product name; ")
            self.quantity = int(input("Quantities: "))
            self.price = float(input("Price: "))
        print("You must register the product first!")        
            
    def remove_product(self):
        pass
    
    def change_product(self):
        pass
    
    def list_product(self) -> list:
        pass
    
    def stock_report(self):
        pass
    
    def close_invetory(self):
        pass