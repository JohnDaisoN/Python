class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1

        return count

'''
this one - too too easy
because of sorted function in python

other one liner code will be 
'''

sum(h1 != h2 for h1, h2 in zip(heights, sorted_heights)) # - zip used to tuplify same indiced elements in 2/>2 lists , sum to act as count var subtitiue