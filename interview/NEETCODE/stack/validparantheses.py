# class Solution:
#     def isValid(s: str) -> bool:
#      stack = []
#      correct = False
#      if len(s) > 1:
#         if s[0] == ']' or s[0] == '}' or s[0] ==  ')':
#             return False
#         for elem in s:
            
#             if elem == '[' or elem == '{' or elem == '(':
#                 stack.append(elem)
#                 correct = False
#             elif elem == ']':
#                 if stack[-1] != '[':
                    
#                     return False
#                 else:
#                     correct = True
#                     stack.pop()
#             elif elem == '}':
#                 if stack[-1] != '{':
               
#                     return False
#                 else:
#                     correct = True
#                     stack.pop()
#             elif elem == ')':
#                 if stack[-1] != '(':
                
#                     return False
#                 else:
#                     correct = True
#                     stack.pop()
                
#      return correct

#     string = input('write parantheses')
#     val = isValid(string)
#     print(val)

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

def redundantparantheses(s):
    stack = []
    operandcount, opcount = 0,0
    for c in s:
        if c.isalnum():
            if not stack[-1].isalnum():
                stack.append(c)

                operandcount += 1
            else:
                return True
        elif c == '(':
            stack.append(c)
            continue
        elif c in '+-*/':
            if stack[-1] in '+-*/':
                return True
            else:
                stack.append(c)
                opcount += 1
        elif c == ')':
            opcount += 1
# def red(str):
#     s = []
#     for i in s:
#         if i = )
#         ele = 0
#         top = s.pop()

#         while 

def makevalid(s):
    Map = {")": "("}
    stack = []
    ans = 0

    for c in s:
        if c not in Map:
            stack.append(c)
            continue
        
        elif stack[-1] == Map[c]:
            stack.pop()
        else:
            ans += 1
            continue


    return len(stack)+ans

string = ')((('
length = makevalid(string)
print(length)


# def c_valid(str):
#     s = []
#     ans = 0
#     for i in s:
#         if i == '(':
#             s.append(i)
#         else:
#             if len(s)>0:
#                 s.pop()
#             else:
#                 ans += 1
        # ans += len(s)
        







