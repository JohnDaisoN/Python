books = [10,20,30,40]
m = 1

l = max(books)
h = sum(books)

def possibleToAllocate(mid):
    noofstudents = 1
    # i = 0
    

    s = 0
    # limit = 0

    for i in books:
        if s + i <= mid:
            s += i
            
            # limit += 1
        else:
            noofstudents += 1
            s = i

        
            
            # limit = i
            # break
    
    # if limit != len(books):
    #     for j in range(limit,len(books)):
    #         while books[j] <= mid and m:
    #             limit += 1
    #             m -= 1

    return noofstudents == m
quantity = 0

while l <= h:
    mid = (l + h)//2
    print(mid)
    if (possibleToAllocate(mid)):
        quantity = mid
        h = mid - 1

    else:
        l = mid + 1

        
        


print( quantity)

