# a = [2, 3, 4,5,6 ,7]
# # b = ["sd", "sf", "fg", 5,6]

# # print(sum(a)/len(a))
# # pre = zip(a,b)

# # # print(dict(pre))




# # print(list(enumerate(a)))


# # a = ['FRANK', 'BOY', 'JASON']

# # print(list(map(lambda x: x.title(), a)))


# # even = list(filter(lambda x:x%2==0, a))
# # print(even)


# aList = [1,2,3,4,5,6,7,8,]
# bList= [98,56,33,40,27,67]

# multiples_3 = list(filter(lambda x:x%3==0, bList))
# print(multiples_3)


# product = max(bList) * min(bList)

# print(product)



# cdict = dict(zip(aList,bList))

# print(cdict)


# c = list(range(3,10))
# print(c)

import time
import random



print('Welcome to this game!')
aList = ['Goat', 'John', 'School', 'Django', 'Bread', 'Meat', 'Chicken']
print(f"Guess a word from the list below:\n{aList}")

user_input = input("Enter your word\n>")

print('Please wait...')

time.sleep(10)

print("....shuffling...")
random.shuffle(aList)

choice = random.choice(aList)

time.sleep(1)
print(3)
time.sleep(2)
print(2)
time.sleep(2)
print(1)
time.sleep(2)
if choice.lower() == user_input.lower():
    print('You win')
else:
    print('Try again next time')
    
print(f'Computer choice is {choice}')