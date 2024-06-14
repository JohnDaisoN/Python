'''
this is medium tough - concept is ok
mine got 55/63 testcases
need to optimize using some other means
i checked duplicality by implementing a 0s array for all elems int he range of the largest element inn nums
i sorted the array
i increment each element by 1 until the element becomes unique , i.e duplicality[elem] = 0, if it is still 1 - then keep on incrementing
'''

class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def unique(elem, supe, c=0):
            while supe[elem] != 0:
                elem += 1
                c += 1
            supe[elem] = 1
            return c

        if not nums:
            return 0

        max_elem = max(nums)
        supe = [0] * (max_elem + len(nums))  # Allocate enough space to handle increments
        count = 0

        for elem in sorted(nums):
            if supe[elem] == 0:
                supe[elem] = 1
            else:
                count += unique(elem, supe)

        return count


'''
lets see optimized leetcoe version

neetcode yayy

1)sorting - nlogn
2) counting sort - n + max(nums)


'''
#simple sort
'''
it was pretty easy 
use two pointers
compare adjacent elements 
the trick is to see how much the right number needs to be incremented

if left elem >= right elem 
we know that left element was incremented
so naturally right is also a duplicate 

'''
class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0

        for i in range(1,len(nums)):
            if nums[i-1] >= nums[i]:
                count += 1 + (nums[i-1]-nums[i])
                nums[i] += 1 + (nums[i-1]-nums[i])

        return count

'''
counting sort
nt coded but only desc

consider original nums, take each value and make a dict of its count


if count of an elem is > 1
find no: of extra copies

move duplicate to next bucket - one opeation - because only 1 copy
next bucket is 2 - now 3 copies
subtract 2 copies - move it to next group

do this continuously
'''


        