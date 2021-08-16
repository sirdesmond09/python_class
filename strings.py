str1 = "this is john"

# print(str1.title())
# print(str1.upper())

# print(str1.startswith("t"))
# print(str1.endswith("n"))

# print(str1.index("z"))
# print(str1.find("z"))


# str2 = "   "

# print(str2.isspace())
# list_of_words = str1.split(" ")

# joined_words = ".".join(list_of_words)
# print(joined_words)



# print("Welcome")
# print("Add two numbers together.")
# num1 = float(input("Enter the first number\n>"))
# num2 = float(input("Enter the second number\n>"))

# print(num1+num2)



########## CLASS WORK CORRECTION #####

# 1. Write a program that gets input from the user and coverts it to uppercase

#Solution

# user_input = input("Enter your word\n>")
# print(user_input.upper())


# #2 Write a program that gets an input from the user and changes all the first letter to upper case
# #solution

# user_input = input("Enter your word\n>")
# print(user_input.title())

# #3 Write a program that gets a sentence from the user as a string and splits it into a string of words
# #solution

# user_input = input("Enter your sentence\n")
# print(user_input.split(" "))


# 4. Write a program that takes in 3 numbers from the user and computes the average.
#solution

num1 = float(input("Enter the first number\n"))
num2 = float(input("Enter the second number\n"))
num3 = float(input("Enter the third number\n"))

average = (num3+num2+num1)/3
print(f"The average is {average}")