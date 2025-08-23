import math

def maxSubArray( nums):
    ans = -math.inf
    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            ans = max(ans, cur_sum)
    return ans

ans = maxSubArray([2,4,3,5,1,3])
print(ans)