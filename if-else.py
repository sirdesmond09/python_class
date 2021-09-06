# import time 


# data = {
#     "username" : "password"
# }


# username = input("Enter your username:\n>")
# password = input("Enter your password:\n>")
# password2 = input("Confirm your password:\n>")

# print("Verfiying username...")
# time.sleep(3)
# if username in data.keys():
#     print("This username already exists")
    
# else:
#     print("Checking passwords...")
#     time.sleep(3)
#     if password == password2:
#         data[username] = password
#         print(f"Creating account for {username}")
#         time.sleep(3)
#         print("Account created successfully")
#     else:
#         print("Please enter matching passwords")
    
    

c = 1

while c <= 10:
    user_input = int(input("Enter your age in number: "))

    if user_input >= 18:
        print('You are eligible to vote')
        
    else:
        print('Not eligible')
        
    print(c)
    print()
    
    c+=1