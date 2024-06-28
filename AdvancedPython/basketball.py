arrray = [1,2,3,4,5]

k = 3

i = 0
sum = 0
csum = 0
returnedsum = 0
for r in range(0,len(arrray)):
    subarray_size = r-i+1
    if subarray_size <= k+1:
        csum = arrray[r] * subarray_size
        sum += csum
        returnedsum = max(sum,returnedsum)
    else:
        sum -= arrray[i] * (subarray_size-k)
        i += 1

print(returnedsum)


