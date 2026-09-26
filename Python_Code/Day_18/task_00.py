# File handeling with python.

# file = open(file="text.txt")    #open a file
# content = file.read()   #read a file
#  print(content)  #print contents of file
# file.close()    #close a file

#In above code we need explecitl declear close a file.
#But in below code we can do easly and don't tell python to close file.

#read a file
with open(file="text_00.txt", mode="r") as file:
    content = file.read()
    print(content)
    
    
#write a file
with open(file="text_01.txt", mode="w") as file:
    file.write("Hello from task_01.txt.")

    