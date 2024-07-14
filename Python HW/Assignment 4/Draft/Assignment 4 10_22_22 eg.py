# importing re module
from pickle import FALSE, TRUE
import re
from turtle import left
test_str = "<a><b><c></c></b></a>"
print("The original string is : " + str(test_str))
reg_str = "<.*?>" 
res = re.findall(reg_str, test_str)
s= "</.*?>"
res_test = re.findall(reg_str,res[2])
print("The Strings extracted : " + str(res))

def valid_html(test_strings):
    tag = '[a-z]'
    for x in range ((len(test_strings))-1):
        if len(test_strings) % 2 == 0 and len(test_strings) > 0:
            for x in range ((len(test_strings))//2): 
                    print("For loop entered: ")
                    s= "</.*?>" 
                    if len(re.findall(s, test_strings[x])) != 0:
                        print("New for Loop entered")
                        if  re.findall(tag, test_strings[x]) == re.findall(tag,test_strings[x-1]):                                                   # Need to check the close tag and the one before is matching
                            test_strings.remove(test_strings[x])
                            test_strings.remove(test_strings[x-1])
                            # if len(test_strings) == 0:
                            #     return True
                            # else:
                            #     return False
        else:
            return False                    
    return True
# printing result
print("'" + test_str + "'" + "," + str(valid_html(res)))



