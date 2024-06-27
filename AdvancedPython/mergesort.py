def mergesort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        mergesort(l)
        mergesort(r)
        merge(l,r,arr)

    return 

def merge(left,right,arr):
    l = 0
    m = 0
    n = 0

    while l < len(left) and m < len(right):
        if left[l] < right[m]:
            arr[n] = left[l]
            l += 1
            n += 1
        else:
            arr[n] = right[m]
            m += 1
            n += 1
    while l < len(left):
        arr[n] = left[l]
        l += 1
        n += 1
    while m < len(right):
        arr[n] = right[m]
        m += 1
        n += 1

    return arr


mergesort([2,5,3,1,4])
