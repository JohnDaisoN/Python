'''
Pattern Printing
Difficulty: BasicAccuracy: 54.24%Submissions: 21K+Points: 1
Given a number N. The task is to print a series of asterisk(*) from 1 till N terms with increasing order and difference being 1.

Example 1:

Input:
N = 3
Output:
* ** ***
Explanation:
First, print 1 asterisk then space after
that print 2 asterisk and space after that 
print 3 asterisk now stop as N is 3
'''

#easier than last one - especially python makes it os effortless
class Solution:
    def printPattern(self, N):
        i = 1
        while i <= N:
            print('*'*i,end="")
            print(' ',end="")
            i += 1