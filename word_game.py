#### TASK 1

# print("Welcome to Word Game")
# print("""
# The rules of the game are:
# 1. Try to guess a word in our system
# 2. Upon getting a word correctly you get 5 points
# 3. If your word appears n times you get n*5 points

# May the best guess win!    
#     """)


# my_random_words = """grenadine: thin syrup made from pomegranate juice; used in mixed drinks
# Demonic: relating to or characteristic of demons or evil spirits.
# hefty: Of considerable weight and size.
# gladiolus: any of numerous plants of the genus Gladiolus native chiefly to tropical and South Africa having sword-shaped leaves and one-sided spikes of brightly colored funnel-shaped flowers; widely cultivated
# Effeminate: (of a man) having characteristics regarded as typical of a woman; unmanly.
# concretize: make something concrete
# manikin: a life-size dummy used to display clothes.
# canvass: get opinions by asking specific questions.
# lubbrly: clumsy and unskilled.
# cordial: politely warm and friendly.
# jocular: characterized by jokes and good humor.
# Utopian: of or pertaining to or resembling a utopia.
# tamp: press down tightly.
# Ecstasy: an overwhelming feeling of great happiness or joyful excitement
# obbligato: a part of the score that must be performed without change or omission.
# woodsy: characteristic or suggestive of woods.
# ha-ha: a loud laugh that sounds like a horse neighing.
# stevedore: a laborer who loads and unloads vessels in a port.
# effervescence: the process of bubbling as gas escapes.
# bromidic: given to uttering bromides.""".lower()


# user_input = input("Enter your guess\n>").lower()
# word_occurance = my_random_words.count(user_input)
# score = word_occurance*5

# print(f"Your score is {score}")

#### TASK 2

#Get input from the user and print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.


# a = int(input("Enter your first number:\n>"))
# b = int(input("Enter your second number:\n>"))

# print(a+b)
# print(a-b)
# print(a*b)


### Task 3 
#Convert "this is a string" to "this-is-a-string"

# string = "this is a string"
# print(string)
# list_of_string = string.split()

# print("-".join(list_of_string))

# # or

# print(string.replace(" ", '-'))


### Task 4
#Get the input from the user and return a string welcoming the user to python

# first_name = input("Enter your first name:\n>")
# last_name = input("Enter your last name:\n>")


# print(f"Hello {first_name} {last_name}! You just delved into python.")


#### DATA STRUCTURES #### 
new_list = ['this', "brown", 55, "oxen", True, 0.85]
# print(new_list[1])
# print(new_list[1:4:2])

# new_list[0] = 59

# print(new_list)

second_list = ['yam', "egg", "fish"]


print(new_list + second_list)


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

first_num = list1[2][2][1]
second_num = list1[2][1]

print(first_num+second_num)