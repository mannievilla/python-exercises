import json

class Atm:
    # a special method that is called when an object is created
    def __init__(self, balance=0, filename='transaction_file.txt'):
        self.balance = balance
        self.filename = filename
    
    def get_balance(self):
        return self.balance

    def set_balance(self, new_balance):
        self.balance = new_balance 

#### copied from below

    def withdraw(self):
        while True:
            try:
                withdraw_input = float(input('How much is the withdrawl?: '))
                if withdraw_input < 0:
                    print('Invalid withdraw amount. Please enter a non-negative value.')
                else:
                    if withdraw_input > self.get_balance():
                        print('Insufficient funds')
                    else: 
                        self.set_balance(self.get_balance()-withdraw_input)
                        operation = { 'name': 'withdraw', 'amount': withdraw_input }
                        self.write_transactions(json.dumps(operation))
                        return self.get_balance()
            except:
                 print('Invalid withdraw amount. Please enter a non-negative value.')
        
    def deposit(self):
        while True:
            try:
                deposit_amount = float(input('How much is the deposit?: '))
                if deposit_amount < 0:
                    print('Invalid deposit amount. Please enter a non-negative value.')
                else:
                    self.set_balance(self.get_balance() + deposit_amount)
                    # first, we create a json object/dictionary object to record the action user takes
                    # then we use json.dumps() to serialize the Python object into a JSON-formatted string to be stored
                    # into the file
                    operation = { 'name': 'deposit', 'amount': deposit_amount }
                    self.write_transactions(json.dumps(operation))
                    return self.get_balance()
            except:
                 print('Invalid deposit amount. Please enter a non-negative value.')
    
    
    def menu_options(self):
        print(f'''\n
        ~~~ Welcome to your terminal checkbook! ~~~
        \n
        \nWhat would you like to do? \n
        \n
        1) view current balance\n
        2) record a debit (withdraw)\n
        3) record a credit (deposit)\n
        4) exit)\n''')

    def exit_display(self):
        operation = { 'name': 'view', 'amount': self.get_balance() }
        self.write_transactions(json.dumps(operation))

    # write the jsonified string operation into the filename.txt
    def write_transactions(self, operation):
        # a+ is used for append and write in an existing file
        with open(self.filename, 'a+') as f:
            f.write(operation + '\n')

    """
        first, it reads in the specified file
        then, it looks into the last line of the file and loads the last line as a json object/diciontary object
        after that, it checks if the value of the 'name' from the dictionary object is view
            if yes, atm object takes in the value of the 'amount' from the object
            if no, truncate the transaction history file; (because there is a transaction error ex. forcefully close
                out the program)
    """
    def read_transactions(self):
        # r+ is used for read and write concurrently in a file
        with open(self.filename, 'r+') as f:
            lines = f.readlines()

            last_line = lines[-1]

            # json.loads() function is used to deserialize a JSON string and convert it into a Python dictionary object
            last_line_json_obj = json.loads(last_line)
            if last_line_json_obj['name'] != 'view':
                f.truncate(0) # deletes file content truncate() if last line does not contain ['view']
            else:
                self.balance = last_line_json_obj['amount']

    # def write_check(self):
    #     while True:
    #         try:
    #             check_input = float(input('amount on check: '))
    #             if check_input < 0:
    #                 print('Invalid Amount. Please try again')
    #             else:
    #                 if check_input > self.get_balance():
    #                     print('Insufficient funds')
    #                 else:
    #                     self.set_balance(self.get_balance() - check_input)
    #                     operation = { 'name': 'check', 'amount': check_input } 
    #                     self.write_transactions(json.dumps(operation)) #serialize to be a JSON string
    #                     return self.get_balance()
    #         except:
    #             print('Invalid check amount. Please enter a non-negative value.')



# trans_line = self.set_balance

# trans_line['balance'] = self.set_balance
# save_transaction(str(transaction), filename)