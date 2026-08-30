# dictionary: is data structure. that exist a form of key: value pair
# we can access value using key but we can't access key using value.
# here we define a dictionary call fruit_dictionary that exist key("apple"): value("red") and more etc.
fruit_dictionary = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow"
}

# access dictionary item using key
print(fruit_dictionary["apple"])

#update item value using key
fruit_dictionary["banana"] = "green"
print(fruit_dictionary["banana"])

# insert a item in dictionart fruit_dictionary
fruit_dictionary["dates"] = "brown"
print(fruit_dictionary["dates"])

# loops through dictionary. here i is act like individual key.
for i in fruit_dictionary:
    print(i)

# loops througn dictionary. here i is act like key and each key gives us value.
for i in fruit_dictionary:
    print(fruit_dictionary[i]) 

# lenght of dictionary
print(len(fruit_dictionary))

# type checking
print(type(fruit_dictionary))

