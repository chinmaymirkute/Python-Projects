#Star pyramid using python code
#Coded by - Chinmay Mirkute
#You can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute


print("Enter Number of Rows to make star pyramid : ")

row = int(input())


for i in range(row):
    
    for s in range(row, i, -1):
        
        print(end=" ")
        
    for j in range(i+1):
        
        print(end="* ")
        
    print()