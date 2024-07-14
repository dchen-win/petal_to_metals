
import json
import requests
import html
from pprint import pp
#Load all the json data from the url 
# get all the category first
# https://opentdb.com/api_category.php   
cat_values = [{"id":21,"name":"Sports"},{"id":22,"name":"Geography"}, {"id":28,"name":"Vehicles"}]

# change dynamic url
url = "https://opentdb.com/api.php?amount=10&category=9"
    
headers = {
        'token': "7aab972af6bea8ce91471835361d488a7fa94ae2147eca5266b336b0bc44a5f2",
        }
    
response = requests.get(url,headers=headers)   
print(response.text)
results = json.loads(response.text)
pp(results)

# Check out the result
print(type(results))
# Check out the elements in the results and get all the keys and values in a
list = []
for i in results :
    list.append(results[i])
print(list)
a = list[1]
print(a[1])
#Append all the categories into list
category_list = []
for s in range(len(a)):
    print("The category list is {} and tye type is {}.".format(a[s]["category"], a[s]["type"]))
    # Only choose the muptiple type questions
    if a[s]["type"] == "multiple":
        category_list.append(a[s])
        # category_list.append(a[s]["category"])
        # category_list.append(a[s]["question"])
print(category_list[0])
# print("Welcome to Trivia Bot 5000, Please Select a Category of Trivia")
# print(type(category_list[0]))
print(category_list[0].keys())

print(len(category_list))
for category in category_list:
    print(category['category'])
    print(category['difficulty'])
print("1" + "." + category['category'].replace("%", ' '))
# print("2" + "." + category_list[1].replace("%", ' '))
# print("3" + "." + category_list[2].replace("%", ' '))
# print(int(input("Please enter a number: ")))
user_input = int(input("Please enter a number: "))
# if user_input == 1:
#     print(f"You pick" + category_list[0].category())
# elif user_input == 2:
#     print(f"You pick" + category_list[1].category())
# elif user_input == 3:
#     print(f"You pick" + category_list[2].category())
#General knowledge
new_url = https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple&encode=url3986










# Why everytime I run the code, it show different data for the index. Why there are repeat category values?
# How to create a empty list and append key and values in the empty list?
# How to tie with what questions you need to ask? Correct answer with line 30? 
# Do I need to use postman to generate url? I already have a url?
# What is the short cut to unindex code?

