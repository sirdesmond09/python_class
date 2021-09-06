import time 
import random

employeeData = {

    "Employees" : [

        {

        "userId":"rirani",

        "jobTitleName":"Developer",

        "firstName":"Romin",

        "lastName":"Irani",

        "preferredFullName":"Romin Irani",

        "employeeCode":"E1",

        "region":"CA",

        "phoneNumber":"408-1234567",

        "emailAddress":"romin.k.irani@gmail.com"

        },

        {

        "userId":"nirani",

        "jobTitleName":"Developer",

        "firstName":"Neil",

        "lastName":"Irani",

        "preferredFullName":"Neil Irani",

        "employeeCode":"E2",

        "region":"CA",

        "phoneNumber":"408-1111111",

        "emailAddress":"neilrirani@gmail.com"

        },

        {

        "userId":"thanks",

        "jobTitleName":"Program Directory",

        "firstName":"Tom",

        "lastName":"Hanks",

        "preferredFullName":"Tom Hanks",

        "employeeCode":"E3",

        "region":"CA",

        "phoneNumber":"408-2222222",

        "emailAddress":"tomhanks@gmail.com"

        }

    ]

}

userId = input('Enter your userId:\n')
jobTitleName = input('Enter your jobTitleName:\n') 
firstName = input('Enter your firstName:\n')
lastName = input('Enter your lastName:\n')
preferredFullName = input('Enter your preferredFullName:\n')
employeeCode = input('Enter your employeeCode:\n')
region = input('Enter your region:\n')
phoneNumber = input('Enter your phoneNumber:\n')
emailAddress = input('Enter your emailAddress:\n')


new_dict = {'userId':userId, 
            'jobTitleName' : jobTitleName, 
            'firstName': firstName, 
            'lastName' : lastName, 
            'preferredFullName' : preferredFullName, 
            'employeeCode' : employeeCode, 
            'region':region, 
            'emailAddress':emailAddress}

employeeData["Employees"].append(new_dict)

print("Creating your profile in the data base....")

time.sleep(2)

print("Almost there...")

time.sleep(3)


print('Created successfully!')


# 2.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

less_than_5 = lambda x: x<5 

print(list(filter(less_than_5, a)))


# 3.

a = list(range(1,10))
user_choice = int(input('Enter a number:\n>'))

random.shuffle(a)

com_choice = random.choice(a)

print('checking results...')
time.sleep(3)


if user_choice > com_choice:
    print("Too high")
elif user_choice < com_choice:
    print("Too low")
elif user_choice == com_choice:
    print("Just right!")

