num_list = [1,-3,-5,3,-9,25,10]
def absolute_value(num):
    return abs(num)
num_list.sort(key = absolute_value)
print(num_list) 
# [1,3,-5,-9,10,25]
