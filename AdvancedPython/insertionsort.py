array = [2,6,12,4,15]

for i in range(len(array)):
    minimum = i
    for j in range(i,len(array)):
        if array[j] < array[i]:
            minimum = j
    array[minimum],array[i] = array[i],array[minimum]
    

print(array)
