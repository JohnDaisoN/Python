'''1190. Reverse Substrings Between Each Pair of Parentheses
Solved
Medium
Topics
Companies
Hint
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.'''

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        def reversestack(stacky,x):
            if stacky[-1] == '(':
                stacky.append(x)
                return stacky
            a = stacky.pop()
            reversestack(stacky,x)
            stacky.append(a)
            # print(stacky)
            return stacky
        def reversetilllastleftbracket(stack):
            if stack[-1] == '(':
                # stack.pop()
                return stack
            x = stack.pop()
            reversetilllastleftbracket(stack)
        
            reversestack(stack,x)
            return stack

        #this is the only non-trivial but easy function

        #it is performed after reversing a substring - we have to eliminate the 
        #left bracket of the corresponing reversal
        #if we choose to do it after full operatyion- wont work because that left bracket
        #will causr anomalies
        #what about during reversal - also cant do because you kind of need that during every recursive call
        #for it to maintain count of which substring to reverse
        #or else it will reverse the entire stack in one turn - which is not what we want
        def removethatleftbracket(stack):
            if stack[-1] == '(':
                stack.pop()
                return stack
            b = stack.pop()
            removethatleftbracket(stack)
            stack.append(b)
            return stack
            
        for elem in s:
            if elem != ')':
                result.append(elem)
            else:
                # print(result)
                reversetilllastleftbracket(result)
                # print(result)
                removethatleftbracket(result)
                # print(result)
        # print(result)
        return ''.join(result)

'''
The actual sad part is that the solution is o(n^2) and space complexity up the roof


I am actually proud of me able to crack my willpower into devising 3 and not kidding- 
actually 3 helper functions for this purpose
it was a stack problem - that was easy

reversing a stack - that alone is a problem - i used 2 helper functions for this purpose

might post easy solution idea later

'''