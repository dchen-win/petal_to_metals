string = 'The [person] looked at the [object] and decided to [thing].'
indices_1 = [index for index in range(len(string)) if string.startswith('[', index)]
indices_2 = [index for index in range(len(string)) if string.startswith(']', index)]
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
print(len(result))

r = 0
# input = []
response = []
for r in range(len(result)):
    a = str(result[r])
    # print(a)
    response.append(str(input("Please enter a" + " "+ a + ":")))
    print(response)
    # input.append(response)
    r = r + 1
print(response)


z = 0
for z in range(len(indices_1)):
    new_string = string.replace(result[z], response[z])   
    z = z + 1
    print(new_string)
    string = new_string
print(string)