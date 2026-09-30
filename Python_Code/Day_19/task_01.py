import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()

print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)

#Challenge: find average temperature. solve using python sum() fn
avg_tmep = sum(temp_list) / len(temp_list)
print(f"Using sum fn: {avg_tmep}")

#Challenge: find average temperature. solve using loops
sum = 0
for i in range(len(temp_list)):
    sum = sum + temp_list[i]
    avg_sum = sum / len(temp_list)
print(f"Using Loops: {avg_sum}")    


#Challenge: find average temperature. solve using pandas .mean()
avg_tmep = data["temp"].mean()
print(f"Using pandas mean: {avg_tmep}")
