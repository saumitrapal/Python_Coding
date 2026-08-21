# BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the person's height squared.
# Convert this sentence into code on line 6. 

print("Welcome To BMI Calculator")

# print(type(input()))    # output is <class 'str'> because by default it's type is string

persionWeight = int(input("Enter Your body weight: \n=>"))  #python default fn input() type is always string that why first we need to convert into integer via python function int()
persionHeight = int(input("Enter Your Height: \n=>"))   #python default fn input() type is always string that why first we need to convert into integer via python function int()


bmiCalculation = persionWeight // (persionHeight ** 2)

print("Your BMI is: ", bmiCalculation)