from src.models.invetory import Invetory
from src.models.product import Product

def Show_menu() -> None:
    print("-" * 10)
    print("Invetory control")
    print("-" * 10)
    
# for description, number in option.items():
#         print(f'{number}-{description}')
        
option  = {
    "Register product": 1,
    "change product" : 2,
    "remove produto": 3,
    "List products": 4,
    "Stock report": 5,
    "Close" : 6    
}    


commands = {
    1 : Invetory.register_product,
    2 : Invetory.change_product,
    3 : Invetory.remove_product,
    4 : Invetory.list_product,
}
Show_menu()