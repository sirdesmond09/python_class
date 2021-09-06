#### SET METHODS #####

a = {3, 4, 5, 6, 7}
b = {3, 4, 2, 10, 8}


# print(a.union(b))
# print(a)
# a.update(b)
# print(a)

# print(a)
# a.discard(10)
# print(a)


# print(a)
# a.remove(10)
# print(a)


##### DICTIONARIES ###

users = {
    'john': 
        {'name': 'John Doe', 
         'class': 'Jss 2', 
         'gender': 'Male', 
         'department': 'Science'
         }, 
    'desmond': 
        {'name': 'Desmond', 
         'class': 'ss3', 
         'gender': 'male', 
         'department': 'Art'
         },
    'our_list': ['Desmond', 'ss3', 'male', 'Art']
}

print("Welcome to our portal")

# username = input("Enter your username\n>")

# users[username] = {}
# name = input("Enter your name\n>")
# class_ = input("Enter your class\n>")
# gender = input("Enter your gender\n>")
# department = input("Enter your department\n>") 


# users[username]['name'] = name
# users[username]['class'] = class_
# users[username]['gender'] = gender
# users[username]['department'] = department

# other_list = ['female', 'Economics', '400']
# # print(users)

# data = users['our_list']
# data.extend(other_list)
# print(users['our_list'])

# #join two dictionariees together
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


# dict1.update(dict2)

# print(dict1)




# # Exercise 3: Access the value of key ‘history’ from the below 

# sampleDict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# score = sampleDict['class']['student']['marks']['history']
# print(score)


#excercise 4: Create a new key called employees and assign it to the list

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

defaults['employees'] = employees
print(defaults)