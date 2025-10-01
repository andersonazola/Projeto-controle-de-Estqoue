from src.models.invetory import Invetory
from src.models.product import Product


Invetory = Invetory()
def user_invetory():
    while True:
        user = int(input("\nWhat do you want to accomplish in the inventory?"))
    
        commands = {
            1: lambda: Invetory.register_product(
                input("Product name: ").lower(),
                float(input("Price U$: ")),
                int(input("Quantity: "))
                ),
            2: lambda: Invetory.change_product(
                input("Product: "),
                input("New product: ").lower()
                ), 
            3: lambda:Invetory.remove_product(
                input("Wich product do you want remove?").lower()
                ),
            4: lambda: Invetory.list_product(),    
        }
        if user in commands:
            commands[user]()
            
        elif user == 5:
            Invetory.close_invetory(input("Are you sure you want to exit inventory? [Y] Yes | [N] Not"))
            break
        
            
        else:
            print("Invalid option")





