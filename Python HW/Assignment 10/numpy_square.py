import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(suppress=True)

#First part: check the maximum sum value for 3 * 3 array and find out (x,y)
numarray = np.loadtxt("C:/Users/15306/Desktop/CS_511 Data Structure/Assignment 10/array-final-2d.txt", dtype = int, delimiter = ",")
myArr = numarray.reshape(50,50)
three_to_three = []
three_to_three_sum_list = []
for i in range(0,48):
    for j in range(0,48):
        three_to_three = three_to_three + [myArr[i:i+3, j:j+3]]
        # print(three_to_three)
        # why it only shows one value if I tried to print outside the loop
        three_to_three_sum = np.sum([myArr[i:i+3, j:j+3]])
        three_to_three_sum_list.append(three_to_three_sum)
#Print the maximum values
print("Maximum Sum: ", end=" ")
print(max(three_to_three_sum_list))
#Print the len of the sum list 48 * 48
#print(len(three_to_three_sum_list))
#Argmax returns the indices of the maximum values along an axis.
#print(np.argmax(three_to_three_sum_list))
print("Coordinate:", end ="(")
print(np.argmax(three_to_three_sum_list)//48, np.argmax(three_to_three_sum_list)%48, end = ") \n")
#Print the 3 * 3 array based on the (x,y)
print("The 3 * 3 array is: ")
print(three_to_three[48*42+42])


# Second part: find out the most frequent sum and the times
def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num, counter
 
print("The most common sum(s) are: ", end=" ")
print(most_frequent(three_to_three_sum_list) [0])
print("They occur: : ", end = " ")
print(most_frequent(three_to_three_sum_list) [1] , end = " ")
print("time")
# the most frequent value is 5154 and it appears 5 times.



