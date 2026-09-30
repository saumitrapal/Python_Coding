import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#find particular squirrel using primary fur color
gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
cinnamon_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrel = data[data["Primary Fur Color"] == "Black"]

#length of squirrel
gray_squirrel_count = len(gray_squirrel)
cinnamon_squirrel_count = len(cinnamon_squirrel)
black_squirrel_count = len(black_squirrel)

#create own dataframe
squirrel_data_count = {
    "Fur color": ["gray", "cinnamon", "black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}
squirrel_data = pandas.DataFrame(squirrel_data_count)

#create csv file
squirrel_data.to_csv("squirrel_count.csv")