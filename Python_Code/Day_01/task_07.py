# TIP CALCULATOR PROJECT    

print("Welcome To Tip Calculator!") #print as it is

totalBill = input("What was the total bill? $")  #take input as string from user

convertTotalBill = float(totalBill) #convert tatalBill string to float number because type or result input fn give us string

# print(convertTotalBill)

tip = input("How much tip would you like to give? 10, 12 or 15? ")  #take input as string from user

converTip = int(tip)    ##convert tip string to int number because type or result input fn give us string

# print(type(converTip))

splitBill = input("How many people to split the bill? ")    

convertSplitBill = int(splitBill)

# print(type(convertSplitBill))

finalBill = (convertTotalBill + (convertTotalBill * (converTip / 100))) / convertSplitBill  #main part of bill calculation

roundOffFinalBill = round(finalBill, 2) #final bill round off upto after two decimal place

print(f"Each persion should pay: ${roundOffFinalBill}")  #print final result using f-string