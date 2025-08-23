

array = 'fiffiifffi'
l = list(array)

for elem in l:
    if elem == 'i':
        elem == 'f'
        pos = array.index(elem)
        l[pos] = 'f'
        break
for elem in l:
    if elem == 'i':
        start = l.index(elem)
        print(start)
        break
j = len(array)-1
while j >= 0:
    if l[j] == 'i':
        end = j 
        print(j)
        break
    j-= 1



print(end-start+1)


