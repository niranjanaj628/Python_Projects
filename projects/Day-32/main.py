import pandas as pd 
import smtplib
import random 
from datetime import datetime

my_email = my_email = "army4life7777@gmail.com"
password= "argo tzzl sxlk qlgs "

today = (datetime.now().month , datetime.now().day)
df = pd.read_csv('Python_Projects/projects/Day-32/birthdays.csv')
df_dict = {(data_row['month'],data_row['day']) : data_row for (index, data_row) in df.iterrows()}


if today in df_dict:
    lr = 'letter_' + str(random.randint(1,3)) + '.txt'
    with open (f'Python_Projects/projects/Day-32/letter_templates/{lr}') as file:
        letter = file.read()
    letter = letter.replace('[NAME]',df_dict[today]['name'])
    
    to_email = df_dict[today]['email']
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password= password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=to_email, 
                        msg= f"Subject: Happy Birthday! \n\n{letter}")
    
      


