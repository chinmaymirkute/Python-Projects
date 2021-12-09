#Password Generator using python code
#By importing the python random module
#Coded by - Chinmay Mirkute
#You can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Hello Guys, Welcome to the python password generator !!!")
print("Enter the data for generating your password.\n")


newletters = int(input("Enter the number of letters to be used in generating password  --> ")) 

newsymbols = int(input(f"Enter the number of symbols to be used in generating password  --> "))

newnumbers = int(input(f"Enter the number of numbers to be used in generating password  --> "))

password_list = []

for i in range(1, newletters + 1):
  password_list.append(random.choice(letters))

for i in range(1, newsymbols + 1):
  password_list += random.choice(symbols)

for i in range(1, newnumbers + 1):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for i in password_list:
  password += i

print(f"Your Randomly generated password is: ")
print("⬇⬇⬇")
print(f"{password}")

print("Thankyou for using ")