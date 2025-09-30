from src.models.invetory import Invetory
from src.models.product import Product
from src.Views.view_creator import commands, option


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



