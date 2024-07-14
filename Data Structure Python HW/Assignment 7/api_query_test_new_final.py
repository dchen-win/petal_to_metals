import json
import requests
import html
from pprint import pp
import random
#Load all the json data from the url 
# get all the category first
# https://opentdb.com/api_category.php   
#cat_values = [{"id":21,"name":"Sports"},{"id":22,"name":"Geography"}, {"id":28,"name":"Vehicles"}]
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
print(id)