#Merging two dict by using python code
#Coded by - Chinmay Mirkute
#You can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute

#adding two dictionaries of vegetables by using python code by merging
Dict_1 = {1: 'Brinjal', 2: 'Eggplant', 3: 'Potato'}
Dict_2 = {4: 'Tomato', 5: 'Radish', 6:'Garlic'}

print("First Dict: \n", Dict_1)
print("Second Dict: \n", Dict_2)

Dict_1.update(Dict_2)

print("Merging two Dict : ")
print(Dict_1)