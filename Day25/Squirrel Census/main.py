# # '''import csv
# #
# # with open("weather_data.csv") as weather_data:
# #     data = csv.reader(weather_data)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(row[1])
# #     print(temperatures)'''
# #
# import pandas as pd
#
# df = pd.read_csv("weather_data.csv")
# #
# # temp_list = df["temp"].tolist()
# #
# # #Get Data in columns
# # print(df["condition"])
# # print(df.condition)
#
# #Get data in Row
#
# # print(df[df["day"] == "Monday"])
# # print(df[df.temp == df.temp.max()])
#
# # monday = df[df.day == "Monday"]
# # monday_temp = monday.temp[0]
# # monday_temp_F = monday_temp * 9/5 + 32
# #
# # print(monday_temp_F)
#
# #Create DF from scratch
#
# data_dict = {
#     "students": ["Amy", "Juna"],
#     "score": [1,2]
# }
#
# df = pd.DataFrame(data_dict)
# df.to_csv("new_data.csv")

import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey = len(df[df["Primary Fur Color"] == "Gray"])
cinnamon = len(df[df["Primary Fur Color"] == "Cinnamon"])
black = len(df[df["Primary Fur Color"] == "Black"])

fur_dic = {
    "Fur Color" : ["grey","red","black"],
    "Count" : [grey, cinnamon, black]
}

df2 = pd.DataFrame(fur_dic)
df2.to_csv("squirrel_count.csv")


