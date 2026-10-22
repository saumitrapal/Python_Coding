# from smtplib import *
# import os
# import dotenv

# dotenv.load_dotenv()

# my_email = os.getenv("EMAIL")
# my_email_password = os.getenv("PASSWORD")

# with SMTP("smtp.gmail.com", 587, timeout=10) as connection:
#     connection.ehlo()
#     connection.starttls()
#     connection.ehlo()
#     connection.login(user=my_email, password=my_email_password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="saumitra31415926@gmail.com", 
#                         msg="Subject: Hello\n\n this is the body of mail.")
#     print("Email Send Successfully.")

import datetime as dt

current_datetime = dt.datetime.now()
current_year = dt.datetime.now().year
current_month = dt.datetime.now().month

print(current_datetime)
print(current_year)
print(current_month)
