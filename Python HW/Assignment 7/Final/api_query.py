import json
import requests
import html
from pprint import pp
import random

cat_values = {"Sports": 21, "Geography": 22, "Vehicles": 28}
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
id = cat_values[user_input]
print(f"You choose ", end = '')
print(user_input, end = ', ')
b = int(input("how many questions do you want? "))     
# change dynamic url
url = (f"https://opentdb.com/api.php?amount={b}&category={id}&type=multiple")
    
headers = {
        'token': "7aab972af6bea8ce91471835361d488a7fa94ae2147eca5266b336b0bc44a5f2"
        }
response = requests.get(url,headers=headers)   
# print(response.text)
results = json.loads(response.text)
# pp(results)
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
# print(category_list)

#Ready to print the questions
counter = 1
for ele in category_list:
    print("Question", end=" ")
    print(counter) # how to assign the value instead of object?
    print(html.unescape(ele['question'])) 
    counter = counter + 1
    #Append the answers to list
    answers = []
    answers.append(ele['correct_answer'])
    for i in range(len(ele['incorrect_answers'])):
        answers.append(ele['incorrect_answers'][i])
    #random change the orders of answers
    random.shuffle(answers) 
    # print(answers)
    count = 0
    for pos, elem in enumerate(answers):
        a = pos + 1
        print(a, elem)
    user_choice = int(input("Choose your answer: "))
    if answers[user_choice-1] == ele['correct_answer']:
        user_correct_anwer = ele['correct_answer']
        print("That is the correct answer!")
        count = count + 1
    else: 
        print("Sorry, that is wrong, the correct answer was ", end = '')
        print(ele['correct_answer'])

print(f"Your game is over, you got {count} out of {b} correct.")
print("Thanks for playing!")

    # HTML characters should be unescaped using the previously mentioned library
    



