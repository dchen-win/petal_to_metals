

filename = 'input.txt'
with open('input.txt') as f:
    string = f.read()
# Find the [] index in the string
indices_1 = [index for index in range(len(string)) if string.startswith('[', index)]
indices_2 = [index for index in range(len(string)) if string.startswith(']', index)]
# Find the string inside []
result = []
i = 0
for i in range(len(indices_1)):
    start = indices_1[i]
    end = indices_2[i]
    substring = string[start+1:end]
    result.append(substring)
    i = i + 1
    print(substring)
print(result)
# Gather end user input and still need to works on save them inside the list
r = 0
for r in range(len(indices_1)):
    a = str(result[r])
    response = str(input("Please enter a" + " "+ a + ":"))
    r = r + 1     
    print(string.rstrip())
f.close()

with open('output.txt','w') as out:
# Working on replace response to the result
        z = 0
for z in range(len(indices_1)):
    new_string = string.replace(result[z], response[z])   
    z = z + 1
    print(new_string)
    string = new_string
    print(new_string)
    out.write(new_string)
out.close()
# hint   
#Open the input txt and search [] by using re package
#Use split function; https://docs.python.org/3/library/stdtypes.html#str.split
#Use replace function first and then replace it with *
# obejct = [cat, dog, eat]
# i = 0
# for i in len(obejct):
#     print("Enter object[i]")
#     i = i + 1