import smtplib
import datetime as dt
import random

with open('Python_Projects/projects/Day-32/Birthday Wisher (Day 32) start/quotes.txt') as file:
    quotes = file.readlines()
    quote = quotes[random.randint(0,101)]

my_email = "army4life7777@gmail.com"
password= "argo tzzl sxlk qlgs "

now = dt.datetime.now()

if now.weekday()==0:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        # transport level security
        connection.starttls()
        connection.login(user=my_email, password= password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="nirandnir7@gmail.com", 
                        msg= f"Subject: Good Morning! \n\nHere's quote of the day:\n\n{quote}\nHave a nice day!")