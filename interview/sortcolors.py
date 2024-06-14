'''itd
juudt an easy way to implement the sorting approach u use
u can use quicksort or mergesort or anything
i chose plain old bubsort
it worked luckily
'''
class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        print(nums)
