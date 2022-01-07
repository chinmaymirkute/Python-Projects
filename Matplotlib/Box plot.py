#Box plot
#Coded by - Chinmay Mirkute
#You can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute

from matplotlib import pyplot as plt
import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [3, 4, 5, 6, 7, 8, 9, 2, 1]
c = [5, 6, 7, 8, 9, 1, 2, 3, 5, 7, 4]

data = list([a, b, c])

plt.boxplot(data)
plt.show