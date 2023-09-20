class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False
        
        first = float('inf')  # Initialize first as positive infinity
        second = float('inf')  # Initialize second as positive infinity
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False
'''
man this is another heartbreaking one
no need to implement three pointers cuz it is stil o(n^2)
do so that in one iteration itself you get all three satisfying numbers or return false- easiest code but i didnt get it tho dog
now can i do it in 0(1)?
'''