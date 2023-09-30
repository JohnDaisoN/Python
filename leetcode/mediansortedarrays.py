class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = []
        n = nums1 + nums2
        n = sorted(n)
        if len(n) % 2 == 0:
            mid1 = n[len(n)//2]
            mid2 = n[len(n)//2 - 1]
            m = mid1 + mid2
            return (m/2.0)
        else:
            return n[len(n)//2]
        