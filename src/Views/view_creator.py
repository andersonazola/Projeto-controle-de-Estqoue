from src.models.invetory import Invetory
from src.models.product import Product
from src.controllers.controller_invetory import user_invetory

def Show_menu():
    print("-" * 15)
    print("Invetory control")
    print("-" * 15)
    
    for description, number in option.items():
        print(f'{number}-{description}')
        

        
option  = {
    "Register product": 1,
    "change product" : 2,
    "remove produto": 3,
    "List products": 4,
    "Close": 5,    
}    


