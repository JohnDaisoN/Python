'''
1482. Minimum Number of Days to Make m Bouquets
Solved
Medium
Topics
Companies
Hint
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1
super tough for me to think of this

basic idea dfor optimization was BINARY SEARCH

its based on the fact that we are checking no: of days taken for k bouquets from day1 to day(max) - so why dont we use binary search to get
min no of days in logn time - efficient instead of looking for every day if flowers bloomed or not

'''
class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def canMakeBouq(bloomDay, mid, k):#helper to check if at 'mid' days are we possible to get k consecutive flowers and get m bouquets
            bouqcount = 0
            consecutivecount = 0

            for elem in bloomDay:
                if elem <= mid:#first if - important concept - to check for consecutiveness property of an array
                    consecutivecount += 1
                else:
                    consecutivecount = 0

                if consecutivecount == k:#second if - concept to check if consecutive flowers are k - then we can make 1 bouq
                    bouqcount += 1
                    consecutivecount = 0
            return bouqcount


        n = len(bloomDay)
        start = 0
        end = max(bloomDay)
        minday = -1#-1 because if array cannot inherently do this at all -- then -1 needs to be returned

        while start <= end:
            mid = start + ((end-start)//2)
            if(canMakeBouq(bloomDay, mid, k)>=m):
                minday = mid
                end = mid - 1#at this stage we find that m bouq of k flowers can be made in 'mid' no of days, nop w e need to cheeck if we can fo it in lesser no of days
                # so end is lowered to mid-1
            else:
                start = mid + 1

        return minday
                

        