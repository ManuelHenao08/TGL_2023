class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount. Amount must be greater than zero.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount. Amount must be greater than zero and less than or equal to the account balance.")
    
    def check_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Class BankAccount with methods deposit, withdraw and check_balance"

def main():
    try:
        # Create a BankAccount instance
        account = BankAccount()

        # Deposit some money by default
        account.deposit(100)
        balance = account.check_balance()

        numbers=[]
        mode = False
        flag = False
        while not flag:
            print("-------")
            print("Welcome Main Menu")
            print("Bank Account -> (1)")
            print("Exit -> (2)")
            user_input = input("Please choose a mode > ")

            if user_input == "1":  # Bank Account
                while not mode:
                    print("-------")   
                    print("Choose the request for your account: ")
                    print("Deposit -> (1)")
                    print("Withdraw -> (2)")
                    print("Check Balance -> (3)")
                    print("Account Info -> (4)")
                    user_input2 = input("Please enter the method > ")
                    if user_input2 == "1" or  user_input2 == "2" or  user_input2 == "3" or user_input2 == "4" :
                        mode = True

                    if user_input2 =="1": #Deposit
                        user_input_value = int(input("Please enter the money you want to deposit > "))
                        balance = account.check_balance()
                        print(f"Balance before deposit: {balance}")
                        account.deposit(user_input_value)
                        print(f"Balance after deposit: {account.check_balance()}")
                    elif user_input2 == "2": #Withdraw
                        user_input_value = int(input("Please enter the money you want to withdraw > "))
                        balance = account.check_balance()
                        print(f"Balance before withdraw: {balance}")
                        account.withdraw(user_input_value)
                        print(f"Balance after withdraw: {account.check_balance()}")
                    elif user_input2 == "3": # Check Balance
                        balance = account.check_balance()
                        print(f"Current balance: {balance}")
                    elif user_input2 == "4": # Account Settings
                        print(f"Account Info: {print(account)}")
                
                mode=False

            elif user_input == "2": #Exit
                flag = True

    except KeyboardInterrupt as error :
        print("\n CTRL-C pressed , thanks for executing advanced_python_1.py script")
    # except:
    #     print("\n Error catched, please try again")

    print("Exit, thanks for executing advanced_python_1.py script")

if __name__ == "__main__":
    main()