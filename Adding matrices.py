#Adding matrices by using python code
#Coded by - Chinmay Mirkute
#You can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute


first_matrix = [[9, 9, 3],
                [5, 6, 1],
                [9, 4, 7]]

second_matrix = [[12, 25, 22],
                 [18, 19, 18],
                 [16, 10, 11]]


result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(first_matrix)):
    
    for j in range(len(first_matrix[0])):
        
        result[i][j] = first_matrix[i][j] + second_matrix[i][j]
        
for r in result:
    print(r)