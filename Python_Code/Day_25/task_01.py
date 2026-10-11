height = float(input("enter height in meter: "))
width = int(input("enter width in kg: "))
bmi = width / height ** 2

print(f"your bim: {bmi}")

if height > 3:
    raise ValueError("Human heigh should not be grater then 3 meter.")