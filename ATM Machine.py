#welcome to ATM MACHINE python code
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute
your_balance = 50000
print("Hey Guys !!! welcome to ATM Machine ")
print("Select Transaction")
print("1-->BALANCE")
print("2-->WITHDRAW")
print("3-->DEPOSIT")
print("4-->EXIT")



selection =float(input("Please select any numbers from above to carry out your transactions "))


if(selection == 1):
    print("Your balance is ", your_balance)


elif(selection == 2):
    withdraw = float(input("Please Enter amount to withdraw "))


    if(your_balance > withdraw):
        total = your_balance - withdraw
        print("success")
        print("Now your account balance is :",total)


    else:
        print("You don't have Sufficient Balance to carry out transaction")


elif(selection == 3):
    deposit = float(input("Please Enter amount to deposit "))
    totalbalance = your_balance + deposit
    print("success")
    print("Now your account balance is: ", totalbalance)


elif(selection == 4):
    exit()


else:
    print("You haven't enter the proper selection, please check your selection and retry again. ")
print("Thanks for using!!!")