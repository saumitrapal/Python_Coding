import pandas
import datetime as dt
import smtplib
import os
import dotenv
import random

dotenv.load_dotenv()
MY_EMAIL = os.getenv("EMAIL")
MY_EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# Read data from csv file
data = pandas.read_csv("./birthdays.csv")
recipient_name = data["name"].head(1).to_string(index=False)
recipient_email = data["email"].head(1).to_string(index=False)
recipient_brith_year = data["year"].head(1).to_string(index=False)
recipient_brite_month = data["month"].head(1).to_string(index=False)
recipient_brith_day = data["day"].head(1).to_string(index=False)
recipient_brith_date = f"{recipient_brith_year}-{recipient_brite_month}-{recipient_brith_day}"

# Date time 
now = dt.datetime.now()
current_date = now.date()

# print(str(current_date) == recipient_brith_date)


if recipient_brith_date == str(current_date):
    # For data from update and read
    with open(file=f"./letter_templates/letter_{random.randint(1, 3)}.txt", mode="r") as file:
        content = [line.replace('[NAME]', recipient_name) for line in file.readlines()]
        email_body_content = ''.join(content)
        # print(email_body_content)
        # For send a email
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as connection:
            connection.ehlo()
            connection.starttls()
            connection.ehlo()
            connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=recipient_email, 
                msg=f"Subject: Birth Wish \n\n {email_body_content}"
                )
            print("Email send successfully.")
