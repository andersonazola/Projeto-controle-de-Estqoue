# from invetory import Invetory

class Product:
    
    def __init__(self, name: str, quantity: int, price: float,):
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def __repr__(self):
        return f"{self.name} | Price: U${self.price} | Quantity: {self.quantity}"