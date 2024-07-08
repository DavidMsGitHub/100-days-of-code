##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime
import pandas
import random
import smtplib

time_now = datetime.datetime.now()



birthdays_list = pandas.read_csv("birthdays.csv")
def main():
    #irchevs random letters
    letters_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    r_letter_template = random.choice(letters_list)

    # karoche aq chekavs tu emtxveva romelime mere amoigebs im lines emails saxels randomul letter templates airchevs shecvlis names im rowshi dafiqsirebuli saxelit
    if int(birthdays_list.day) == int(time_now.day) and int(birthdays_list.month) == int(time_now.month):
        that_one = birthdays_list[birthdays_list.day == time_now.day]
        email = that_one["email"]
        name = that_one["name"].values[0]



        PLACEHOLDER = "[NAME]"
        main_letter = f"./letter_templates/{r_letter_template}"


        with open(main_letter, "r") as letter:
            MAIN_LETTER = letter.read()
            MAIN_LETTER = MAIN_LETTER.replace('[NAME]', str(name))


        #--------EMAIL tema brat---------
        my_email = "dato2006213@gmail.com"
        password = "beun zvmh vbmj rlvl"
        connection = smtplib.SMTP('smtp.gmail.com', port=587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: Happy Birthday Dear {name}\n\n {MAIN_LETTER}"),

while True:
    main()



