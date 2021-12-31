# Multiplication of Two Matrices by using python code
# Coded by - Chinmay Mirkute
# You can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute


A = [[9, 5, 4],
     [1, 2, 6],
     [8, 5, 7]]
B = [[2, 4, 4],
     [6, 1, 3],
     [4, 6, 4]]

the_result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]


for m in range(len(A)):

   for n in range(len(B[0])):

          for o in range(len(B)):

               the_result[m][n] += A[m][o] * B[o][n]


print("The multiplication of matrix A and B is: ")
for result in the_result:
   print(result)