'''1509. Minimum Difference Between Largest and Smallest Value in Three Moves
Medium
Topics
Companies
Hint
You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.'''
'''
this is actually i am not gwtting the concwpt
in a simple manner i executed one idea and passed like 23/61 testcases

that one was trivial 
'''
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 4:
            return 0#because 3 changes were allowed so any array of length qual to 
            #or less than 4 can change remaining 3 elements to thatg fourth element 
            #so all elements are qual - max- min = 0
        else:
            x = min(nums)
            n = sorted(nums)#here idea is that
            #i sort nums, take largest 3 elements - make it minimum
            n[-1],n[-2],n[-3] = x,x,x

            print(n)
            answer = max(n) - x#then in new sorted nums , i return the new maximum and already ex
            #existent minimum's difference
            return answer

'''
explanation in MP-5 SUMMER BIRD

BASICALLY - OONLY 4 POSSIBILITIES FOR 2 POITNERS - FROM LEFT END, RIGHT END - U CAN REMOVE
(0,3),(1,2),(2,1) AND(3,0) CJARACTERS TO MAKE IT MINIMUM 0 CHECK FOR MIN RESUKT
'''
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 4:
            return 0
        else:
            nums.sort()
            res = float('inf')
            for l in range(4):
                r = len(nums) - 4 + l
                res = min(res,nums[r]-nums[l])

            return res

#FOR O(N) SOLUTION - HEAPIFY - NSMALLEST, NLARGEST

        