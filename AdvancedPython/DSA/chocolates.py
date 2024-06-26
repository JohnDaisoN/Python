l = [2,0,14,9,0,0,5]
i, j = 0,0#two pointer
# 'i' pointer goes till end of list to check for next non-zero element and 'j' points to the position where that ith element needsa to be placed
while i < len(l):
    if l[i] != 0:#non zero eleemtn found
        l[j] = l[i]#copy that element to the jth position
        j += 1#increment both pointers
        i += 1

    else:
        i += 1#still zero - so i increment to find non-zero

for elem in range(j,len(l)):
    l[elem] = 0#now j is at end of all non -zero , so from j till length of list, all elements are made 0

print(l)
    
        


