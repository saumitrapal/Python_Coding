# Find Bug and Debuging

#Problem_00:
def fn():
    for i in range(1, 20):
        #if i == 20: # this line create bug because range fn start 1 and end it 19 this line never print.
            #print("You got it")
        if i == 19:
            print("You got it!")

fn()


user_input = int(input("Enter you brith date: "))

if 2000 <= user_input <= 2005:
    print("Hey Hello 2000's")
else:
    print("Hey Hello Newbies")


print(range(0, 10))

