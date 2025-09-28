from src.models.invetory_repository import invetory

def Show_menu() -> None:
    print("-" * 10)
    print("Invetory control")
    print("-" * 10)
    
    
option  = {
    "Register product": 1,
    "Product entry":2,
    "Remove product" : 3,
    "Change produto": 4,
    "List products": 5,
    "Stock report": 6,
    "Close" : 7,
    
}    

Show_menu()

