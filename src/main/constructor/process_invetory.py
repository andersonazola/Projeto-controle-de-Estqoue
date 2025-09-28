from src.models.invetory_repository import InvetoryControl

def Show_menu() -> None:
    print("-" * 10)
    print("Invetory control")
    print("-" * 10)
    
# for description, number in option.items():
#         print(f'{number}-{description}')
        
option  = {
    "Register product": 1,
    "Product entry": 2,
    "Remove product" : 3,
    "Change produto": 4,
    "List products": 5,
    "Stock report": 6,
    "Close" : 7    
}    


commands = {
    1 : InvetoryControl.register_product,
    2 : InvetoryControl.product_entry,
    3 : InvetoryControl.remove_product,
    4 : InvetoryControl.change_product,
    5 : InvetoryControl.list_product,
    6 : InvetoryControl.stock_report,
}
Show_menu()
while True:
    try:
        user_invetory = int(input("What do you want to accomplish in stock? "))
        if user_invetory in commands:
            commands[user_invetory]()
        
        elif user_invetory == 7:
            print("leaving the invetory....")
            break   
        else:
            print("Sorry, type any of the commands above to perform any invetory activity.") 
    except ValueError:
        print("Invalid command. Please enter number only.")
