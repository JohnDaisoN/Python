'''52. Grumpy Bookstore Owner
Medium
Topics
Companies
Hint
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the d'''
#i didnt have the strength to think all of this up

#basically so no my solution only 


class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        l = 0#left pointer
        window, max_window = 0,0#window - current window size where we want to 
        satisfied = 0#actually satisfied people that no matter if grumpy or noy
        for r in range(len(customers)):#right pointer expands window only if 
            if grumpy[r]:
                window += customers[r]#only if grumpy is 1 - we need to expand window
            else:
                satisfied += customers[r]

            if r - l + 1 > minutes:#check if window size exceeded minuted 
                if grumpy[l]:#then we check if the first element of the grumpy is grumpy element 
                    window -= customers[l]#onlly then we need to loosed it - or else we 
                l += 1#should increment 1 until size decreases or we meet grumpy elements
            max_window = max(window, max_window)#we want maximum sizzed window - thats why

        return satisfied + max_window
        