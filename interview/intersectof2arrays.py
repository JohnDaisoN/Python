'''
definitely there will be better solutions that this

i just used a count dictionary and stored count of values appearing in smaller array
then took each elem in bigger array and if it is having a count of 1 or > 1 - append it
in array - and then decrement the count of the value in the count dictionary

maybe there might be some simpleleelelele code out there
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        array = []
        if len(nums1) > len(nums2):
            k = nums2
            l = nums1
        else:
            k = nums1
            l = nums2
        
        count = {}
        # elem_count = 0

        for elem in k:
            if elem in count:
                count[elem] += 1
            else:
                count[elem] = 1
        for elem in l:
            if elem in count and count[elem] >= 1:
                array.append(elem)
                count[elem] -= 1