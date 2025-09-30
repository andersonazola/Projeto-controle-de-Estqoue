
#  invetory = []
# from product import Product


class Product:
    
    def __init__(self, name: str, quantity: int, price: float,):
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def __repr__(self):
        return f"{self.name} | Price: U${self.price} | Quantity: {self.quantity}"
            
        
        
class Invetory:        
    def __init__(self):
       self.product = []
       
    # registrar produto
    def register_product(self, product, price, quantity): 
        self.product.append({"product": product, "price": price, "quantity": quantity})
        
    
#     # adcionar produto
#     def product_entry(self, product_add):
#         self.product_add = str(input("which product do you want to add? "))
#         if product_add in invetory:
#             self.product = input("Product name; ")
#             self.quantity = int(input("Quantities: "))
#             self.price = float(input("Price: "))
#         print("You must register the product first!")
        
        
    # Alterar produto            
    def change_product(self, old_product: str, new_product: str):
        old_product = str(input("Which product do you want to change?"))
        for i in self.product:
            if i['product'] == old_product:
                new_product = str(input("What new product? ")).lower
                i['product'] == new_product
                print("product successfully changed")
                return
            print("This product is out of invetory.")
                
            
        
    def remove_product(self, remove_item):
        remove_item = str(input("Wich product do you want remove?"))
        if remove_item in self.product:
            self.product.remove(remove_item)
            print("Product remove successfully! ")
        print("this product is out of stock. ")            
            
                          
    
    def list_product(self, option: str) -> list:
        option = str(input("Do you want to see the invetory? [Y] Yes | [N] Not: "))
        if option.upper == 'Y':
            for item in self.product:
                print(f"\nProduct: {item['product']} - Price: R${item['price']} - Quantity: {item['quantity']}")
    
#     def stock_report(self):
#         pass
    
#     def close_invetory(self):
#         pass