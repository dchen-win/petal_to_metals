# My original code
import time
import random
data_list = []
for x in range(5000):
    data_list.append(random.randrange(1,5000,2))

start = time.process_time() 

# Replace the below code with your program to time it
#def abs_sort(data_list):
    #Create empty list
temp_data_list = data_list.copy()
new_list = []
while temp_data_list:
    #Set index 0 as the minimum value
    minimum = temp_data_list[0]
    #Compare other values with the first one, if less than minimum, assign the value to minimum  
    for x in temp_data_list: 
        if abs(x) < abs(minimum):
                minimum = x
        #Positive value will less the negative value
        elif x >= 0 and abs(x) == abs(minimum):
                minimum = x
                
    #Add values in the new list
    new_list.append(minimum)
    #Remove values from the original list
    temp_data_list.remove(minimum)    
# print(new_list)
# Replace the above code with your program to time it

end = time.process_time() 
print("Time elapsed was " + str(end-start))

###################################################################

# My updated code
import time
import random
data_list = []
for x in range(5000):
    data_list.append(random.randrange(1,5000,2))
start = time.process_time() 

# Replace the below code with your program to time it
import json
import requests
import html
from pprint import pp

def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

    # print(random.randrange(1,500000,2))

    # HTML characters should be unescaped using the previously mentioned library
# Replace the above code with your program to time it
insertionSort(data_list)
# for i in range(len(data_list)):
#     print ("% d" % data_list[i])
end = time.process_time()  
print("Time elapsed was " + str(end-start))






