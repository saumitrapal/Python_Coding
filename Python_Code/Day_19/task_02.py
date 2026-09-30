import pandas

#Challenge: find max item in a serice using pandas max()
data = pandas.read_csv("weather_data.csv")
max_temp = data["temp"].max()

# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * (9/5) + 32

print(monday_temp_F)