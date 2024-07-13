string = 'The [animal] looked at the [object] and decided to [verb].'
replace_test_1 = string.replace("[", "*")
replace_test_2 = replace_test_1.replace("]", "*")
print(replace_test_2)

count = 0
for letter in replace_test_2:
    if(letter == '*'):
        count += 1
print(count,'letters found')
length = count // 2
print(length)

result = []

start = replace_test_2.index('*')
end = replace_test_2.index('*',start+1)
start_1 = replace_test_2.index('*',start+2)
end_1 = replace_test_2.index('*',start+3)
substring = replace_test_2[start+1:end]
substring_1 = replace_test_2[start+2:end_1]
result.append(substring)
result.append(substring_1)
print(f"Start: {start}, End: {end}")
print(substring)
print(substring_1)
print(result)