responses = []
while True:
    response1 = input("Please provide a animal:")
    responses.append(response1)
    response2 = input("Please provide an object:")
    responses.append(response2)
    response3 = input("Please provide a verb:")
    responses.append(response3)
    break
filename = 'input.txt'
with open('input.txt') as f:
    contents = f.read()
    print(contents.rstrip())
f.close()

with open('input.txt','w') as out:
    for response in responses:
        out.write(f"The {responses[0]} looked at the {responses[1]} and decided to {responses[2]}.")
    out.close()
    
#reference: https://ehmatthes.github.io/pcc_2e/solutions/chapter_10/