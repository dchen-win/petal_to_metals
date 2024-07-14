#Create abs sort function
def abs_sort(data_list):
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
    return new_list

# num_list =   [-16, 16, -1, 1, 2, -2]
# print("original list = ", num_list)
# new_list = abs_sort(num_list)
# print("Required output = 1, -1, 2, -2, 16, -16")
# print("sorted_list =", new_list) 
# print("Check original list unsorted = ", num_list)






# Creating a abs sort in place function  
def abs_sort_in_place(list1):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)-1): 
        #Compare the 2 values next to each other 
        for j in range(len(list1)-1):  
            if(abs(list1[j])>abs(list1[j+1])):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp
                #Positive value is smaller than negative value
            elif (list1[j]) < 0 and abs(list1[j]) == abs(list1[j+1]): 
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp

       
num_list =  [5, -2, 10, -13, 2, 20]  
# print(abs_sort_in_place(num_list))
