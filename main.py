##################### Normal Starting Project ######################
from datetime import datetime
import pandas as pd
import random as r
import smtplib
MY_EMAIL="senddertest@gmail.com"
MY_PASSWORD="dewchnovjtaiucby"
today = datetime.now()
today_tuple=(today.month, today.day)
data=pd.read_csv("birthdays.csv")
birthdays_dict={(data_row["month"], data_row["day"]): data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person=birthdays_dict[today_tuple]
    file_path=f"letter_templates/letter_{r.randint(1,3)}.txt"
    try:
       with open(file_path) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])
       print("Letter template loaded and personalized.")
    except Exception as e:
       print(f"Error reading the letter template:{e}")
       exit()
    try:
       with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(
             from_addr=MY_EMAIL,
             to_addrs=birthday_person["email"],
             msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
       print("Email sent successfully.")
    except smtplib.SMTPAuthenticationError:
       print("Failed to authenticate with the email server. Check your email and app password.")
    except smtplib.SMTPConnectError:
       print("Failed to connect to the email server. Check your network connection.")
    except smtplib.SMTPRecipientsRefused:
       print("The recipient email address was refused. Check the recipient's email.")
    except Exception as e:
       print(f"Failed to send email: {e}")
else:
    print("No birthdays today.")