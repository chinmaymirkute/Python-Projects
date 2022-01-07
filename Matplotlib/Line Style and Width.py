#Line Style and Width
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute

import numpy as np
from matplotlib import pyplot as plt
a = np.arange(25,60)
b = 2*a
plt.plot(a,b, color = 'r', linestyle = ':' , linewidth = 4) 
#you can use your color according to your desire
plt.title("X-axis VS Y-axis")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()