# importing re module
from pickle import FALSE, TRUE
import re
from turtle import left
example_set = ['''<a><b><c></c></b></a>''',
 '''<foo>asd<bar>alksjd</bar><p>asldkj</p></foo>''',
 '''<foo><bar></bop></bar></foo>''',
 '''<foo><bar></bar></foo></foo>''',
 '''<foo><bar></foo></bar>''']
print(type(example_set))
print("The original string is : " + str(example_set))
reg_str = "<.*?>" 
print(len(example_set))
# res = re.findall(reg_str, example_set[2])
# new_list = []
# new_list_update = new_list.append(res)
# print(new_list_update)
x = 0
new_list = []
for x in range(len(example_set)):
    # res = re.findall(reg_str, example_set[x])
    # print(res)
    new_list_update= new_list.append(re.findall(reg_str, example_set[x]))
    x = x + 1
print("The updated string is : " + str(new_list))
