##################### Extra Hard Starting Project ######################
import smtplib
import pandas
import datetime as dt
import random

my_email = "joshuaonudemy@gmail.com"
my_password = "xclv ilqp stis ewod"
templates = [
        "letter_templates/letter_1.txt",
        "letter_templates/letter_2.txt",
        "letter_templates/letter_3.txt",
    ]


# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
records = data.to_dict("records")






# 2. Check if today matches a birthday in the birthdays.csv
birthdays = {(item["month"],item["day"]):item for item in records}
now = dt.datetime.today()
month = now.month
day = now.day
birthday_check_tuple = (month,day)
birthday_person = {}
if birthday_check_tuple in birthdays:
    birthday_person = birthdays[birthday_check_tuple]
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


    with open(random.choice(templates),"r") as f:
        letter_contents = f.read()
        final_email_text = letter_contents.replace("[NAME]", birthday_person["name"])



    # 4. Send the letter generated in step 3 to that person's email address.


    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday\n\n {final_email_text} ")



