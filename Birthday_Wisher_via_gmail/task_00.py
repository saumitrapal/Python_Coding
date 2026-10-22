import datetime as dt
import smtplib
import random
import os
import dotenv

dotenv.load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
MY_EMAIL_PASSWORD = os.getenv("PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_ADDRESS")


# For random quote 
with open(file="quotes.txt", mode="r") as quotes_file:
    quotes_list = [quotes for quotes in quotes_file]
    random_quote = random.choice(quotes_list)
    # print(random_quote)
    
# For current date
now = dt.datetime.now()
today_date = now.date()
today_day = now.strftime('%A')

    
# For sand email
if today_date:
    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=5) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()
        connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=RECIPIENT_EMAIL, 
            msg=f"Subject:{today_day} Motivation Quote\n\n{random_quote}"
            )
        print("Email send successfully.")
        

