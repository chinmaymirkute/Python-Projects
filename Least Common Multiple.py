#Least Common Multiple in python
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute


def least_common_multiple(a, b):

   
   if a > b:
       greater = a
   else:
       greater = b

   while(True):
       
       if((greater % a == 0) and (greater % b == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

print("The least common multiple is", least_common_multiple(num1, num2))