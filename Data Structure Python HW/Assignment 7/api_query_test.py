import json
import requests
import html
from pprint import pp
import random
#Load all the json data from the url 
# get all the category first
# https://opentdb.com/api_category.php   
cat_values = [{"id":21,"name":"Sports"},{"id":22,"name":"Geography"}, {"id":28,"name":"Vehicles"}]
# cat_values = {"Sports": 21}
print("Welcome to Trivia Bot 5000, Please Select a Category of Trivia")
print("1.Sports")
print("2.Geography")
print("3.Vehicles")
user_input = int(input("Please enter a number: "))
if user_input == 1:
    user_input = 'Sports'
elif user_input == 2:
    user_input = 'Geography'
elif user_input == 3:
    user_input = 'Vehicles'
# id = cat_values[user_input]
b = int(input("how many questions do you want? "))
# for cat in cat_values:
#     if cat['id']== user_input:
#         print(f"You picked " + cat['name'] + "," ,end=" ")
#         print(b)
        
# change dynamic url
url = (f"https://opentdb.com/api.php?amount={b}&category={user_input}&type=multiple")
    
headers = {
        'token': "7aab972af6bea8ce91471835361d488a7fa94ae2147eca5266b336b0bc44a5f2"
        }
response = requests.get(url,headers=headers)   
print(response.text)
results = json.loads(response.text)
pp(results)
#Clean the data and get initial start
list = []
for i in results :
    list.append(results[i])
# print(list)
a = list[1]
# print(a[1])
# print(len(a))

#Clean the data and only leave dictionary in the list
category_list = []
for s in range(len(a)):
    category_list.append(a[s])
print(category_list)

#Ready to print the questions
counter = 1
for ele in category_list:
    print("Question", end=" ")
    # for index in range(b):
    #     a = index + 1
    #     print(a)
    print(counter) # how to assign the value instead of object?
    print(ele['question'])
    counter = counter + 1
    answers = []
    answers.append(ele['correct_answer'])
    for i in range(len(ele['incorrect_answers'])):
        answers.append(ele['incorrect_answers'][i])
    print(answers)
    random.shuffle(answers) 
    print(answers)
    




    # Should I manually type the index number for the questions? user input enter will be +1 for my index?
    # --the order keep change if I do random, I should change to compare the the value?
    # HTML characters should be unescaped using the previously mentioned library
    



