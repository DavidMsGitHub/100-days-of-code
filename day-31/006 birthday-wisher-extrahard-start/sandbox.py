import pandas

birthdays_list = pandas.read_csv("birthdays.csv")

that_one = birthdays_list[birthdays_list.day == 22]
name = that_one["name"].values[0]
print(name)