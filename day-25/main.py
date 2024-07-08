#
# import csv
#
#
# with open("weather_data.csv", "r") as datas:
#     data = csv.reader(datas)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#
# print(temperatures)
import pandas


#
# temp_list = data["temp"].to_list()
#
# summary = sum(temp_list)
#
# average = sum(temp_list) / len(temp_list)
#
# max = data["temp"].max()
#
# print(data[data.temp == max])
# print(max)fgf

data = pandas.read_csv("squirrel_data.csv")

grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "colors": ["gray", "cinnamon", "black"],
    "count": [grey_count, red_count, black_count]
}


data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_color_analysis.csv")

