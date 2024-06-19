'''633. Sum of Square Numbers
Solved
Medium
Topics
Companies
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.'''

'''
it is medium because it is intuitive - you need to understand like a^2 + b^ 2 = c means bruteforce would require you searhcing in o(c^2) complexity 
checking if for any a and any b , sum holds ot not . we reduce this to like 0(c) complexity by computing elements only in range (0,sqrt(c))
because we are not checking for a, b but for a^2, etc.. the space complexity is very bad because we can use a set to store all elements in range (sqrtc)
and then compute their sqaures - as a set for b. so now only one loop needed that is we only need to check for a value -"a" so 


while a^2 less or equal to c 
we can check for any valid b present or not




'''
# space - 0(sqrtc). time - 0(sqrtc)

class Solution(object):
    def judgeSquareSum(self, c):

        square = set()

        for elem in range(int(sqrt(c))+1):
            square.add(elem * elem)

        a = 0
        while a * a <= c:
            target = c - a*a
            if target in square:
                return True
            a += 1
        return False
        """
        :type c: int
        :rtype: bool
        """
        
#optimal other soliton maybe
