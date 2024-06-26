def binsearch(arr,target):
    arr.sort()
    l = 0
    r = len(arr)-1
    mid = 0
    while l <= r:
        mid = l + ((r-l)//2)
        if target == mid:
            print('Target has been found')
            break
        elif target < mid:
            r = mid - 1
        else:
            l = mid + 1

binsearch([2,4,3,1,5],1)
