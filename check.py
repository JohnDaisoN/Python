string = input("Enter the string")
split = string.split()
print(split)
for index,char in enumerate(string):
    if char.isalpha():
        i = index

print(i)

indices = [index for index, char in enumerate(string) if char.isalpha()]
true = string[indices[0]:indices[-1]]
print(true)
