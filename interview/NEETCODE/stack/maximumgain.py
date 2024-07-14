'''

Code
Testcase
Testcase
Test Result
1717. Maximum Score From Removing Substrings
Solved
Medium
Topics
Companies
Hint
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s
'''
class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        self.s = s
        
        def remove_pairs(pair, score):
            
            res = 0
            stack = []

            for c in self.s:
                if c == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    res += score
                else:
                    stack.append(c)
            self.s = "".join(stack)
            return res

        res = 0
        pair = "ab" if x > y else "ba"
        res += remove_pairs(pair,max(x,y))
        res += remove_pairs(pair[::-1],min(x,y))

        return res

'''
ideas - use stacking for removing top element - like valid parantheses i suppose
performing 2 phases - first one for the string having higher points

self.s = for strings - needed because strings are immutable

more drawings on mp5 green bird book
'''
        