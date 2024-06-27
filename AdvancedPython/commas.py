#done when milestones ave a patterned repetition between them like AP or GP
import math
num = 1010000
count = 0
l = len(str(num))#finding length
if l>= 3:
    q = l // 3#finding no of commas in number

for i in range(1,q+1):#for number of commas that can maximum occur
    power = 3 * i
    if num > 1000**(i+1):#if number is greater than the i th  upper limit
        # print(int(('9'* 3) * (i+1)))
        

        count += i * ((1000**(i+1)) - math.pow(10,power))
        # print(count)
    else:
        count += i * (num - math.pow(10,power)+1)
        # print(count)
        

print(int(count))

'''sir
solution below


'''


n = 1010000
curr = 1000
c = 1
ans = 0

while curr <= n:
    next = curr * 1000#next milestone stores
    diff = min(next-curr,n-curr+1)#key point
    #above - we check if calculating current value - min limit or max limit - current value is better -r takes
    #least computationa;l time3 to calculate
    ans += diff * c#c multiplied to account for number of cmmas 
    curr = next#next iteration looks only from current max limit to next max limit 
    c += 1#for 2 coommas, n commas 





