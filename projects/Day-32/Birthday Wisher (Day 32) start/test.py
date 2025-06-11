# import smtplib

# my_email = "army4life7777@gmail.com"
# password= "argo tzzl sxlk qlgs "

# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     # transport level security
#     connection.starttls()
#     connection.login(user=my_email, password= password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="nirandnir7@gmail.com", 
#                         msg= "Subject: GiHellorl \n\n This i sthe body of the email.")
# # connection.close()

import datetime as dt

now=dt.datetime.now()
print(now.day)
print(now.weekday())
print(now)

today = dt.datetime(year=2025, month=4, day=16)
print(today)