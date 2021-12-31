#Area of Triangle using python code
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute


a = float(input("Please Enter 1st side value: "))
b = float(input("Please Enter 2nd side value: "))
c = float(input("Please Enter 3rd side value: "))


s = (a + b + c) / 2


area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('\nArea of triangle is %0.2f' %area)