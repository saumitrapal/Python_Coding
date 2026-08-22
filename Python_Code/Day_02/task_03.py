# BMI CALCULATOR WITH NESTED CONDITION
print("Welcome To BMI Calculator!") #print as it is


weight = int(input("Enter your weight: "))  #takes user input as string and convert type into integer.
height = float(input("Enter your height: "))    #tasks user input as string and convert type into integer.

bmi = weight / (height ** 2)    #BMI calculation 
roundOffBmi = round(bmi, 2) #round off BMI calculation


# print(roundOffBmi)

if roundOffBmi < 18.5:  #condition for below 18.5
    print("Underweight.")
elif roundOffBmi >= 18.5: # condition for exactly 18.5
        if roundOffBmi < 25:    #condition for below 25
            print("Normalweight.")
        elif roundOffBmi >= 25: #condition for exactly 25 and 25 above
            print("Overweight.")

