#Calendar generator using python code
#Coded by - Chinmay Mirkute
#You can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute
import calendar
year_choice = int(input("Enter the year of which calendar you want to see ↡\n"))
month_choice = int(input("Now Enter the Month ↡\n"))


year = year_choice 
month = month_choice    

#printing calendar 

print(calendar.month(year, month))
print("Thanks for using")
