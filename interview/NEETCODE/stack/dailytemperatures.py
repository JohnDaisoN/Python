class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                te, ind = stack.pop()
                result[ind] = i - ind
            stack.append((t,i))

        return result

'''
easy ily understable 

you initiate a specific stack to code the approach - push element - keep pushing until temp becomes greater than last pushed element - 
then pop until temperatures is not greater 

it is similar to like SLR code parsing - almost jk
'''