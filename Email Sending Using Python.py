#Send Email using python code
#Coded by - Chinmay Mirkute
#You can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute


import smtplib
my_email = "your email id"
password = "your password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="recipient email id",
        msg="Subject:Hey there !\n\n This is a python code to send emails"
    )
