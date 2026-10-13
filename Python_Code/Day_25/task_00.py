# Error Handeling try and except

try:
    file = open(file="a.txt")
    dictionary = {"key": 1}
    print(dictionary["key"])
except FileNotFoundError:
    file = open(file="a.txt", mode="w")
    file.write("Hello Python!")
except KeyError as key_error:
    print(f"That key {key_error} is not exits")
else:
    content = file.read()
    print(content)
finally:
    raise KeyError("this key was found")
    