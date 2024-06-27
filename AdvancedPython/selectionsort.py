array = [12,11,5,13,6]
for i in range(len(array)):
    key = array.pop(i)#popping done to get a enxtra space for insert function to work its magic later
    j = i - 1
    while j >= 0 and array[j] > key:
        j -= 1
    array.insert(j+1,key)#that previously ppopped SPACE will be used 

print(array)