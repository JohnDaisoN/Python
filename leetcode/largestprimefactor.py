import math
class Solution:
 def largestPrimeFactor (self, N):
        


    max_prime = 2
    
    while N % 2 == 0:
        N //= 2
    
    for i in range(3, int(math.sqrt(N)) + 1, 2):
        while N % i == 0:
            N //= i
            max_prime = i

    if N > 1:
        max_prime = N
    
    return max_prime