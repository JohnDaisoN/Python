'''
Code
Testcase
Testcase
Test Result
1248. Count Number of Nice Subarrays
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays'''

'''
today no headache - so tried to code- getting many logic - 
but i think htere might be better way or maybe my code is incorrct
but i think i got like 60 % of it 

time for neetcode

'''
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        sub_window = 0
        count = 0
        odd_count = 0
        r = 0
        while r != len(nums) - 1:
            
            if nums[r] % 2 == 1:
                # sub_window += 1
                odd_count += 1
            # else:
                # sub_window += 1
            if odd_count == k:
                count += 1
                # supra = r
                
            
                while nums[r+1] % 2 == 0:
                    count += 1

                    r += 1
                while nums[l] % 2 == 0:
                    count += 1
                    l += 1
                odd_count -= 1
                r += 1

        return count
                

'''
optimal solition exp

so basically i am proud to say that i sort of realized that i might reqire an additional pointer

and seems like the deadly 3 pointer sliding window is nto a dream , but a reality


'''
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0#store total subsets 
        odd = 0#odd count
        l=0
        mid=0
        for r in range(len(nums)):
            if nums[r] % 2:#if number is dod
                odd += 1
            while odd > k:#when odd goes above k  we need to eliminate numbers by l ++ 
                if nums[l] % 2:#in special case where left is odd, we also have to decrement odd
                    odd -= 1
                l += 1#common case 
                mid = l#because mid minimum should be atleast l , or above l 
            if odd == k:#crucial case when odd equals k 
                while not nums[mid] % 2:#here mid pointer comes useful because it checks until the first odd number is reached
                    mid += 1
                res += (mid-l)+1#here mid accounts for al subarays consisting of current window of k 1s
        return res


                



        

        