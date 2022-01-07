#Adding subplots
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute


from matplotlib import pyplot as plt
import numpy as np

x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95]
a = [4, 15, 10, 2, 4, 18, 19, 15, 10, 2]
b = [4, 4, 10, 11, 11, 7, 2, 18, 17, 12]

plt.subplot(1,2,1)
plt.scatter(a,b, marker ='+', c = 'r', s = 100)

plt.subplot(1,2,2)
plt.scatter(a,b, marker ='|', c = 'b', s = 200)
plt.show()