import smtplib
import datetime as dt
import random


MY_EMAIL = "starzcodetest@gmail.com"
PASSWORD = "codetest"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0: # (i.e) 0 means monday
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        server.login("starzcodetest1@gmail.com","codetest")
        server.sendmail(    
            "starzcodetest@gmail.com", 
            "starzcodetest2@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )





