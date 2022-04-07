import smtplib
import datetime as dt
import random as r

# ---------- Account Info ---------- #
my_email = "ezonechess@gmail.com"
password = "Testing123!"
to_email = "ian_koh93@hotmail.com"

now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt", 'r') as file:
    quote = r.choice(file.readlines())

if day_of_week == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:The Thursday Email Blast\n\nThe Quote of the day is:\n\n{quote}"
        )

