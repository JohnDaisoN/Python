
'''
my solution very space efficient but not time eddicient at all - just simple sliding window with multiple iterations
over the nums when r reaches end , l updates to l + 1 and r updates to l+r -> greedy ver very greedy

topis that wouldbe needed - prefix sum( vimp), hashmap(dictionary_)

question
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.



code is straightforward
no comments for that case
'''
class Solution(object):
    def checkSubarraySum(self, nums, k):
        if len(nums) < 2:
            return False
        else:
            l = 0
            r = 1 
        while l < r and l+1 != len(nums):
            if sum(nums[l:r+1]) % k == 0:
                return True
            elif r != len(nums) - 1:
                r += 1
            else:
                l += 1
                r = l + 1

        return False

'lets see an optimal solution buz my only solved 83 /99 testcases - tl exceeded'
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}  
        cumulative_sum = 0
        
        for i, num in enumerate(nums):
            cumulative_sum += num
            remainder = cumulative_sum % k
            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i
        return False
'''
above solution is complex for normal thinking - but relies on the 
remainders procured when dividing cumulative sums with k - if same remainder is 
spotted twice in an interval of min 2 - return True 
'''