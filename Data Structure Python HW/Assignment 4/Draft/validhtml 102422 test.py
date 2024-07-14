from pickle import FALSE, TRUE
import re
# example_set = ['''<a><b><c></c></b></a>''',
#  '''<foo>asd<bar>alksjd</bar><p>asldkj</p></foo>''',
#  '''<foo><bar></bop></bar></foo>''',
#  '''<foo><bar></bar></foo></foo>''',
#  '''<foo><bar></foo></bar>''']
example_set = ['''<foo><bar></foo></bar>''']
# print("The original string is : " + str(example_set))
reg_str = "<.*?>" 
# x = 0
# new_list = []
# for x in range(len(example_set)):
#     new_list_update= new_list.append(re.findall(reg_str, example_set[x]))
#     x = x + 1
# print("The updated string is : " + str(new_list))

def valid_html(test_strings):
        x = 0
        new_list_updated = []
        for x in range(len(test_strings)//2):
            tag = '[a-z]'
            s= "</.*?>"
            for x in range ((len(test_strings))//2):
                print("Enter for0")
                if len(test_strings) % 2 == 0:
                    for x in range ((len(test_strings))//2 + 1): 
                            print("Enter for1")
                            s= "</.*?>" 
                            if len(re.findall(s, test_strings[x])) != 0:
                                if len(test_strings) > 0:
                                        if  re.findall(tag, test_strings[x]) == re.findall(tag,test_strings[x-1]):                                                   # Need to check the close tag and the one before is matching
                                            test_strings.remove(test_strings[x])
                                            test_strings.remove(test_strings[x-1])  
                                        else:
                                            new_list_updated.append((test_strings[x], False)) 
                                # else:
                                #     new_list_updated.append((test_strings[x], True))                   
                else:
                    new_list_updated.append((test_strings[x], False)) 
                        
        else:
            new_list_updated.append((test_strings[x], True))
        return new_list_updated
# for x in range(len(test_strings)):
#     # print("'" + str(example_set[4]) + "'" + "," + str(valid_html(new_list[4])))
#     # a = "'" + str(example_set[x]) + "'" + "," + str(valid_html(new_list[x]))
#     new_list_updated.append(test_strings[x])
# # printing result

print(valid_html(example_set))

