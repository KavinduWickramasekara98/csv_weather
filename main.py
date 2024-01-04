# with open("./weather_data.csv") as weather_file:
#     data=weather_file.readlines()
#     print(data)
 #import csv
# import csv
#
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures=[]
#     for row in data:
#         if row[1]!="temp":
#             temperatures.append(row[1])
#
#     print(temperatures)

import pandas

df = pandas.read_csv("weather_data.csv")
print(df["temp"].mean())


print(df[df.temp==df.temp.max()])

