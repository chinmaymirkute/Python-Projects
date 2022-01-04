#Lowercase to Uppercase in python
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute


print("Enter the Character: ")
char = input()

Letters = ord(char)
Letters = Letters-32
Letters = chr(Letters)
print("Uppercase is: ", Letters)