import smtplib

my_email = "ezonechess@gmail.com"
password = "Testing123!"
to_email = "ian_koh93@hotmail.com"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="")
connection.close()
