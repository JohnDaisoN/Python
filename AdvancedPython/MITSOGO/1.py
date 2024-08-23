string = 'ABCDEFGH'
n = 2
mydict = {key:'' for key in range(1,n+1)}
print(mydict)
counter = 1
i = 0
while i != len(string):
    while counter <= n and i != len(string):
        mydict[counter] += string[i]
        counter += 1
        i += 1
    counter -= 2
    while counter >= 1 and i != len(string):
        mydict[counter] += string[i]
        counter -= 1
        i += 1
    counter += 2
    # i += 1
    
    
# print(mydict.values())

result = ''
for elem in mydict.values():
    result += elem

print(result)

    
