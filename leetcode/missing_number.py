class Solution(object):
    def missingNumber(self, nums):

        nums = sorted(nums)
        
        counter = 0
        for elem in nums:
            if elem == counter:
                counter += 1
            else:
                value = counter

        return counter