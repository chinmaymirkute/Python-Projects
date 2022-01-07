#Plotting two lines in same graph
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute

import numpy as np
from matplotlib import pyplot as plt
a = np.arange(25,60)
b = 2*a
b1 = 2*a
b2 = 4*a
plt.plot(a,b1, color = 'r', linestyle = ':', linewidth = 3) 
plt.plot(a,b2, color = 'b', linestyle = ':' ,linewidth = 2) 
plt.title("Two lines in plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()