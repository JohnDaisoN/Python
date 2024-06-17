'''330. Patching Array
Hard
Topics
Companies
Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.'''
# next hard ---ughhgh
# my idea ->

'''

we takr an gvien array - find sum of all subsets
then also insrtantiate an array from range of 1 to given n -> new
for each elem in new array , if elem is not in given array - make a new list - append that new element, add that elem to every one of the subsets and then append new lsit to new array 

repeatedly till all elements in new arry present in sum of all subsets

but order will go 2 raised to n to find susbets - 

BETYER SOLUTION??

'''
class Solution(object):
    def minPatches(self, nums, n):

        i, output, upto = 0,0,0
        N = len(nums)
        while upto<n:
            if i < N and nums[i] <= upto+1:
                upto += nums[i]
                i += 1
            else:
                output += 1
                upto += (upto+1)
        return output



        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
'''
above solution is super optmal
man i almost wen thsi path also 

the theory is like
given is sorted array, 
so take first elem - with that we can maximum reach sum of upto that elem

next elem might be like 3 , we can add an elem as long as that new element is exceeding our current upto by 1


HIGHLY INTUITUVE
'''