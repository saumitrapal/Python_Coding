class User():
    
    #constructor
    def __init__(self, id, username):
        self.user_id = id 
        self.user_name = username
    
# create a object with providing id, username argument
user1 = User("001", "angela")
user2 = User("002", "jack")

# printing id, username using user_id, user_name attribute
print(user1.user_id, user1.user_name)
print(user2.user_id, user2.user_name)