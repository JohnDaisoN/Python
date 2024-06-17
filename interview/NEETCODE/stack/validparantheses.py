class Solution:
    def isValid(s: str) -> bool:
     stack = []
     correct = False
     if len(s) > 1:
        if s[0] == ']' or s[0] == '}' or s[0] ==  ')':
            return False
        for elem in s:
            
            if elem == '[' or elem == '{' or elem == '(':
                stack.append(elem)
                correct = False
            elif elem == ']':
                if stack[-1] != '[':
                    
                    return False
                else:
                    correct = True
                    stack.pop()
            elif elem == '}':
                if stack[-1] != '{':
               
                    return False
                else:
                    correct = True
                    stack.pop()
            elif elem == ')':
                if stack[-1] != '(':
                
                    return False
                else:
                    correct = True
                    stack.pop()
                
     return correct

    string = input('write parantheses')
    val = isValid(string)
    print(val)

'''apparentlt avobe solition is very big - not fit for a stakc easy problem - still i failed ;)(((('''
#below is right slution
'''
stack - implemennt a pair wise dictionary , check if stack still contains elements
'''
'''
key point - empty array returns true
non empty array so should return false
so correct input therefore needs to popped off till empty 
'''
class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack