
def add(num1, num2):
#addition

   return num1 + num2

def subtract(num1, num2):
#subtraction

   return num1 - num2

def multiply(num1, num2):
#multiplication

   return num1 * num2

def divide(num1, num2):
#division

   return num1 / num2

print("Hey Guys Welcome to calculator.py, here you can calculate your desired operations")
print("Press + to Addition")
print("Press - to Subtraction")
print("Press * to Multiplication")
print("Press / to Division")

#using choice method
choice = input("Enter choice( + , - , * , / ):")

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

#using float so we can even enter those number which has decimals in it

if choice == '+':
   print(num1,"+",num2,"=", add(num1,num2))
   

elif choice == '-':
   print(num1,"-",num2,"=", subtract(num1,num2))
   

elif choice == '*':
   print(num1,"*",num2,"=", multiply(num1,num2))
   

elif choice == '/':
   print(num1,"/",num2,"=", divide(num1,num2))
   
else:
   print("You had not enter the valid input please try entering valid input")