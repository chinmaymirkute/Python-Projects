#Bar - plot
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute

from matplotlib import pyplot as plt
import numpy as np
Learner = {'Raj':37, 'Rahul':94, 'Karan':44, 'Advait':65, 'Ranvijay':35}
Names = list(Learner.keys())
Scores = list(Learner.values())
#add colors as per your choice
plt.bar(Names, Scores, color = 'r')
plt.title("Learner Score")
plt.xlabel("Learner's Name")
plt.ylabel("Scores of Learners")
plt.grid(True)
plt.show()
