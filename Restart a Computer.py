#Restart a Computer using python code
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute


import os

restart = input("Do you want to restart your computer ? (yes / no): ")

if restart == 'no':
	exit()
else:
	os.system("shutdown /r /t 1")
