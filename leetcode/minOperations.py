class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target_sum = sum(nums) - x
        if target_sum == 0:
            return len(nums)
        
        left, max_len, curr_sum = 0, -1, 0
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum > target_sum and left < len(nums):
                curr_sum -= nums[left]
                left += 1
                
            if curr_sum == target_sum:
                max_len = max(max_len, right - left + 1)
        
        return len(nums) - max_len if max_len != -1 else -1


        #super sliding window

        '''
        first logic
        we might think it is very difficult because we might initially thinl there are so many ways, 
        because it is not just selecting the max element from  both ends and minusing it froom x
        no no
        because maybe you delete one from left
        you might have a super good second value in right but it was in second position so it will never get noticed\\

            so somany solautions o(n2 approach)

        so other way is to know that we have to find a series of elements
        whose sum will equal x, so that that sum, which sis y , x-y =0 or x

        so other way is to find the series of contiguous elements which will equal to sum - x
        so that removing thrm from total sum ---    sum - (sum-y) = y = x and we get it\

        now finding continious substring:

        easy:)
        sliding window inm variable approach

        we initialize bpoth left and right as 0 and increment right
        we also add that element to a currentsum and check if it is greater than sum-y
        if yes, then left pointer moves forward to decrease xurrent sum

        at each stage we check if no: of elements left is min 
        and we return its length of array- sliding window size

        Happy
        '''