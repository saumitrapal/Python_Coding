# nested dictionary with list inside
travel_log = {
    "france": ["paris", "lille", "dijon"],
    "germany": ["Berlin"]
}

# access liile city(lille) from the frist item(france).
# print(travel_log["france"][1]) 

# nested list with list
nested_letter = ['A', 'B', ['C', 'D']]
# print the letter 'C'
# print(nested_letter[2][0])


# nested dictionary with dictionary with lists
travel_log = {
    "france": {
        "cities_visited": ["paris", "lille", "dijon"],
        "total_visited": 10
        },
    "germany": {
        "cities_visited": ["Berlin", "Harmburg", "Stuttgart"],
        "total_visited": 6
    }
}

# print stuttgart
print(travel_log["germany"]["cities_visited"][2])