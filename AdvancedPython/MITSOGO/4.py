arr1 = [2,3,5,8]
arr2 = [10,12,14,16,18,20]

size1 = len(arr1)
size2 = len(arr2)
tsize = size1 + size2

if tsize % 2 == 1:
    if size1 % 2 == 0:
        arr = arr1
        ar = arr2

    else:
        arr = arr2
        ar = arr1
    
    elem1 = arr[len(arr)//2]
    elem2 = arr[len(arr)//2+1]
    elem3 = ar[(len(arr)+1)//2]
    lis = [elem1,elem2,elem3]
    lis.sort()
    median = lis[1]
    
    
elif tsize % 2 == 0:
    elem1 = arr1[size1//2-1]
    print(elem1)
    elem2 = arr1[size1//2]
    print(elem2)

    elem3 = arr2[size2//2-1]
    print(elem3)
    
    elem4 = arr2[size2//2]
    print(elem4)

    lis = [elem1,elem2,elem3,elem4]
    lis.sort()
    median = (lis[1]+lis[2])//2

print(median)
    


    
        
