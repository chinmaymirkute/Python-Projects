# Leap Year in python
#Coded by - Chinmay Mirkute
#You can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute

def CheckLeapYear(Year):  
   
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
         
    print("This is a leap Year");  
  
  else:  
    print ("This is not a leap Year")  

Year = int(input("Enter the number: "))  
 
CheckLeapYear(Year)  