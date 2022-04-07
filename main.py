import smtplib
import datetime as dt

# ---------- Account Info ---------- #
my_email = "ezonechess@gmail.com"
password = "Testing123!"
to_email = "ian_koh93@hotmail.com"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=to_email,
#         msg="Subject:Hello\n\nThis is the body of my email!"
#     )

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
print(f"{year}, {month}, {day} and {day_of_week} starting on monday as 0")

date_of_birth = dt.datetime(year=1993, month=8, day=14)
print(date_of_birth)
