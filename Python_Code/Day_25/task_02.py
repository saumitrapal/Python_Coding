fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    # if index > 2:
    #     raise IndexError("index error")
    
    if index > 3:
        try:
            fruit = fruits[index]
            print(fruit + "pie")
        except IndexError as index_error:
            print(f"{index_error}")
    
make_pie(4)
