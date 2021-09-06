my_list = [ "The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]

print(" ".join(my_list))



new_list= ['this', "brown", 55, "oxen", True, 0.85]
# change of value
print(new_list[4])
new_list[4]= False
print(new_list[4])


list1 =[10, 20, [300, 400, [5000, 6000], 500], 30, 40]
first_num=list1[2][2][0]
print(first_num)
second_num= list1[2][3]
print(first_num + second_num)