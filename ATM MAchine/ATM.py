class Atm:
     def __init__(self):
          self.pin = ""
          self.balance = 0 #give balance 0 at starting
          self.menu()
     def menu(self):
          user = input("""
               Select Any 1 operation
               1. Press 1 to create pin
               2. Press 2 to Deposit Money
               3. Press 3 to Withdraw Money
               4. Press 4 to Check Available Balance
               5. Press 5 to Exit
               """)
          if user == "1":
               self.create_pin()               
          elif user == "2":
               self.deposit()
          elif user == "3":
               self.withdraw()
          elif user == "4":
               self.check_balance()
          else:
               print("Exiting...\n Exited Successfully.\n")
     def create_pin(self):
          self.pin = input("Enter your Pin\n")
          print("Pin Successfully set\n")
     def deposit(self):
          temp = input("Enter your Pin\n")
          if temp == self.pin:
               amount = int(input("Enter amount\n"))
               self.balance = self.balance + amount
               print("Deposit Successful\n")
          else:
               print("Pin Entered was wrong\n")
     def withdraw(self):
          temp = input("Enter your Pin\n")
          if temp == self.pin:
               amount = int(input("Enter amount\n"))
               if amount < self.balance:
                    self.balance = self.balance - amount
                    print("Amount Withdrawed Successfully\n")
               else:
                    print("Insufficient Amount\n")
          else:
               print("Pin Entered was wrong\n")
     def check_balance(self):
          temp = input("Enter your Pin\n")
          if temp == self.pin:
               print(self.balance)
          else:
               print("Pin Entered was wrong\n")
          
