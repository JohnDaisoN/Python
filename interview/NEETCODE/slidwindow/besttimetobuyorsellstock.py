class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        lowest = prices[0]

        for elem in prices:
            if elem < lowest:
                lowest = elem
            res = max(res, elem-lowest)
        return res

'''
this above i understook logic - i coded
easy problem- but seemed intuitive

bettwe understand only if yu drow a graph and all - 

basic idea

l - left ppinter - day we buy - we need that to be as minimum as possible - 
initially l = prices[0], we update l only if we see an elem, lesser than it

right pointer is not needed explicitly because one for loop acts as right pointer because we increment it one by one eaxch turn - basic for loop

profit accumulated will be equal to maximum of current profit, and new profit - current elem - left pointer(day we buy)
'''