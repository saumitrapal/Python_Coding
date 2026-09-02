# cli blog applications

art =  '''
====================================
        TERMINAL BLOG MANAGER
====================================
[1] Write a New Post
[2] View Specific Post Using Number
[3] Delete Specific Post Using Number
====================================
'''

import replit 

blog_list = []

def write_blog():
    continue_blog = True
    
    while continue_blog:
        user_input = input("Enter y or n to write a new blog: ")
        if user_input == 'y':
            usr_titel = input("Enter titel: ")
            usr_content = input("Enter content: ")
            usr_date = input("Enter date: ")
            
            blog_dictionary = {
                "titel": usr_titel,
                "content": usr_content,
                "date": usr_date
            }
            blog_list.append(blog_dictionary)
        else:
            continue_blog = False
    
def view_post():
    read_blog = (int(input("Enter the post number you want to read: ")) - 1)
    print(blog_list[blog]) 
          
def delete_blog():
    usr_delete = (int(input("Enter the number post you want to delete: ")) - 1)
    blog_list.pop(usr_delete)
            

blog = True
while blog:
    print(art)
    usr_number = input("Enter you choice (1-3): ")
    
    if usr_number == "1":
        write_blog() 
    elif usr_number == "2":
        view_post()  
    elif usr_number == "3":
        delete_blog()
    else:
        blog = False
        print("Sorry! enter number in between 1 to 3")
        
    