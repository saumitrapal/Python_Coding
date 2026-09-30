import pandas

#create your own dataframe in pandas
data_dict = {
    "name": ["ana", "jon", "ron", "alex"],
    "score": [70, 80, 50, 60]
}

data = pandas.DataFrame(data_dict)
print(data)

#challenge: turn dataframe into csv file.
data.to_csv("data.csv")