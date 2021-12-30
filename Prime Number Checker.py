#welcome to Prime Number Checker python code
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute
the_number = int(input(" Please Enter any Number which you want to check: "))
count = 0

for i in range(2, (the_number // 2 + 1)):
    if (the_number % i == 0):
        count = count + 1
        break

if (count == 0 and the_number != 1):
    print(" %d is a Prime Number" % the_number)
else:
    print(" %d is not a Prime Number" % the_number)