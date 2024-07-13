my_variable = int(input("Enter a Number "))
num = 1
for i in range(my_variable):
    if num % 3 == 0 and num % 5 == 0:
        print(str(num) + " Fizz Buzz")
    elif num % 3 == 0:
       print(str(num) + " Fizz")
    elif num % 5 == 0:
       print(str(num) + " Buzz")
    else:
        print(str(num))
    num = num + 1
print("Done!")