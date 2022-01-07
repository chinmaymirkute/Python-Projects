#Changing Color of graph 
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute

from matplotlib import pyplot as plt
import numpy as np

a = np.arange(25,60)
b = 2*a
plt.plot(a,b, color = 'r') 
#you can use your color according to your desire
plt.show()