#Pie chart
#Coded by - Chinmay Mirkute
#You can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute


from matplotlib import pyplot as plt
import numpy as np

computer_languages = ['Java', 'C++', 'C#', 'JavaScript', 'PHP', 'Python']
percentage = [31.3, 9.4, 10.8, 11.3, 12.4, 24.8]

plt.pie(percentage, labels = computer_languages)
plt.show()