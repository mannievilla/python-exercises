from application import Atm # this includes all the functions defined inside Atm class
import ast
import pandas as pd

def options():
    atm_obj = Atm()

    # read the last line of transaction to set up the Atm object's balance
    atm_obj.read_transactions()

    while True:
        atm_obj.menu_options()
        user_input = input('Your choice: ')
        if user_input.isdigit() and int(user_input) > 4:
            print('Invalid choice')
            
        if user_input.isdigit():
            
            if int(user_input) == 1:
                print('current balance: ', atm_obj.get_balance())
                
            if int(user_input) == 2:
                atm_obj.withdraw()
            if int(user_input) == 3:
                atm_obj.deposit()
            if int(user_input) == 4:
                atm_obj.exit_display()
                break

options()