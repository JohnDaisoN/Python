res = str(input())
lis = res.split(' ')
str1,str2 = lis[0],lis[1]
s = set(elem for elem in str2)
count = 0
for elem in s:
    count += str1.count(elem)
print(count)