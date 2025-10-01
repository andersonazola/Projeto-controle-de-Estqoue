

class Invetory:        
    def __init__(self):
       self.product = []
       
    # registrar produto
    def register_product(self, product, price, quantity): 
        self.product.append({"product": product, "price": price, "quantity": quantity})
        print("Product registered successfully!")
        
    
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
        for i in self.product:
            if i['product'] == old_product:
                i['product'] == new_product
                print("product successfully changed")
                return
            print("This product is out of invetory.")
                
            
        
    def remove_product(self, remove_item):
        if remove_item in self.product:
            self.product.remove(remove_item)
            print("Product remove successfully! ")
        print("this product is out of stock. ")            
            
                          
    
    def list_product(self) -> list:
        for item in self.product:
            print(f"\nProduct: {item['product']} - Price: R${item['price']} - Quantity: {item['quantity']}")
    
#     def stock_report(self):
#         pass
    
    def close_invetory(self, confirm):
        from src.controllers.controller_invetory import user_invetory
        
        if confirm == 'Y':
            print("leaving invetory...")
            
        else:
            print("Returning to menu")
            return user_invetory()