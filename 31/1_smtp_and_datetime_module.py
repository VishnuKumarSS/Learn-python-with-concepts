# example for usderstanding the datetime and the smtplib module

# # smtp - simple message transfer protocol

# import smtplib
# # here for this just create a dummy account for sending the mails. and make the accounts as less secure in the account settings , so that we can send the message.

# my_email = "starzcodetest1@gmail.com"
# password = "codetest"

# with smtplib.SMTP("smtp.gmail.com") as connection:  # or connection = smtplib.SMTP("smtp.gmail.com")
#     connection.starttls()   # transport layer security
#     connection.login(user = my_email, password= password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="starzcodetest2@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of the code."
#     )


# or


# with smtplib.SMTP_SSL("smtp.gmail.com",465) as connection:
#     connection.login("starztestcode1@gmail.com", "codetest")
#     connection.sendmail(
#         from_addr="starztestcode1@gmail.com",
#         to_addrs="starztestcode2@gmail.com",
#         msg="Subject:Hellow\n\nThis is the body of the code."
#     )





# import datetime as dt

# now = dt.datetime.now()
# print(now)
# year = now.year
# print(year)
# month = now.month
# print(month)

# day_of_the_week = now.weekday()
# print(day_of_the_week) # here 0 means monday, 1 means tuesday, etc...

# #we can print everything by calling the now object that we have created manually above.

# date_of_birth = dt.datetime(year=2001, day= 8,month=7)
# print(date_of_birth)




