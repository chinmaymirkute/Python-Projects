#Fibonacci Sequence Using Recursion 
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute


def recursion_fibo(n):  
    
   if n <= 1:  
       return n  
   else:  
       return(recursion_fibo(n-1) + recursion_fibo(n-2))  


nterms = int(input("Input the terms? "))  


if nterms <= 0:  
   print("Enter Positive Number")  
else:  
   print("Fibonacci sequence is:")  
   for i in range(nterms):  
       print(recursion_fibo(i))  