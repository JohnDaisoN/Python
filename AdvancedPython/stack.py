import math
class stack:
    def __init__(self):
        self.stack = []

    def push(self,val):
        self.stack.append(val)
        return self.stack
    def top(self):
        if self.stack:
            return self.stack[-1]
    def pop(self):
        if self.stack:
            return self.stack.pop()

stack1 = [1,2,3,4]
# stack1.push(1)
# stack1.push(2)
# stack1.push(3)
# stack1.push(4)
# # print(stack1)
# stack2 = stack()
# while stack1.stack:#STACK1 IS OBJECT, WE NEED TO ACCESS ITS STACK
#     x = stack1.pop()# queue differing in the order of popped elements
#     stack2.push(x)
# while stack2.stack:
#     a = stack2.pop()
#     print(a)
# l = [2]

# s = stack()
# s.push(l,4)
# s.push(l,3)
# s.push(l,1)

# print(l)

# print(s.top(l))

#queue using stack

# class queue(stack):
#     def __init__(self):
#         super().__init__()
#         self.stack1 = stack()
#         self.stack2 = stack()
#     def enqueue(self,val):
#         if len(self.stack1) == 0:
#             self.stack1.push(val)
#         else:
#             a = self.stack1.pop()
#             whi
#             self.stack2.push(a)

stack2 = stack()

def addatbottom(stack1,val):
    stack2 = stack()
    while stack1.stack:#we give parameter as objects, so emptying should check on its stack attribute
        x = stack1.pop()
        stack2.push(x)
    stack1.push(val)
    while stack2.stack:# and not on the object itself
        y = stack2.pop()
        stack1.push(y)
    return stack1

# s = stack()
# s.stack = [1]#we initiate a stack accessing stack objects's stack attribute - bit confusing
# s.push(2)# only now we initiate s.stack, push operations work now on s.stack
# s.push(3)
# s.push(4)

# addatbottom(s,9)
# print(s.stack)#simply printing s means we are accessing only the object which cant be printed in basic terms
# we need to print its specific stack attribute
def recursivereversal(stack):
    if not stack.stack:
        
        return 
    x = stack.pop()
    stack.stack = [x] + recursivereversal(stack.pop())
    stack.push(x)
    return stack

def recursiveaddatbottom(stack,val):
    if not stack.stack:
        stack.push(val)
        return stack
    stack.pop()
    x = stack.pop()
    
    recursiveaddatbottom(stack,val)
    

    
    stack.push(x)
    return stack
def addatend(s,val):
    if len(s.stack) == 0:
        s.push(val)
        return s
    top = s.pop()
    addatend(s,val)
    s.push(top)
    return s

def rev(s):
    if len(s.stack) > 0:
        top = s.pop()
        rev(s)
        addatend(s,top)

    return s

# s = stack()
# s.stack = [1]#we initiate a stack accessing stack objects's stack attribute - bit confusing
# s.push(2)# only now we initiate s.stack, push operations work now on s.stack
# s.push(3)
# s.push(4)
# rev(s)
# print(s.stack)

def nextgreatest(arr,val):#the only way
    '''
   i got the solution is baclwards

   variations - next greatest , next smallest, prev gratest, prev smallest

   made by 
    '''
    dic = {}
    stack = [-1]
    
    i = len(arr)-1
    stack.append(arr[i])
    dic[arr[i]] = -1
    i -= 1

    while i >=0:
        if arr[i] < stack[-1]:
            dic[arr[i]] = stack[-1]
            stack.append(arr[i])
            i -= 1
            continue
        else:
            while arr[i] > stack[-1]:
                if stack[-1] == -1:
                    dic[arr[i]] = -1
                    break
                stack.pop()
                
            dic[arr[i]] = stack[-1]
            stack.append(arr[i])
            i -= 1
    return dic

def prevsmallest(arr,val):#the only way
    '''
   i got the solution is baclwards

   variations - next greatest , next smallest, prev gratest, prev smallest

   made by 
    '''
    dic = {}
    stack = [-1]
    
    i = 0
    stack.append(arr[i])
    dic[arr[i]] = -1
    i += 1

    while i < len(arr):
        if arr[i] > stack[-1]:
            dic[arr[i]] = stack[-1]
            stack.append(arr[i])
            i += 1
            continue
        else:
            while arr[i] < stack[-1]:
                if stack[-1] == -1:
                    dic[arr[i]] = -1
                    break
                stack.pop()
                
            dic[arr[i]] = stack[-1]
            stack.append(arr[i])
            i += 1
    return dic
def prevgreatest(arr,val):#the only way
    '''
   i got the solution is baclwards

   variations - next greatest , next smallest, prev gratest, prev smallest

   made by 
    '''
    dic = {}
    stack = [-1]
    
    i = 0
    stack.append(arr[i])
    dic[arr[i]] = -1
    i += 1

    while i < len(arr):
        if arr[i] < stack[-1]:
            dic[arr[i]] = stack[-1]
            stack.append(arr[i])
            i += 1
            continue
        else:
            while arr[i] > stack[-1]:
                if stack[-1] == -1:
                    dic[arr[i]] = -1
                    break
                stack.pop()
                
            dic[arr[i]] = stack[-1]
            stack.append(arr[i])
            i += 1
    return dic
def nextsmallest(arr,val):#the only way
    '''
   i got the solution is baclwards

   variations - next greatest , next smallest, prev gratest, prev smallest

   made by 
    '''
    dic = {}
    stack = [-1]
    
    i = len(arr)-1
    stack.append(arr[i])
    dic[arr[i]] = -1
    i -= 1

    while i >=0:
        if arr[i] < stack[-1]:
            dic[arr[i]] = stack[-1]
            stack.append(arr[i])
            i -= 1
            continue
        else:
            while arr[i] < stack[-1]:
                if stack[-1] == -1:
                    dic[arr[i]] = -1
                    break
                stack.pop()
                
            dic[arr[i]] = stack[-1]
            stack.append(arr[i])
            i -= 1
    return dic







       

    return dic[val]
arr = [29,12,2,3,14,6,18]
d = nextgreatest(arr,12)
l = nextsmallest(arr,12)
prev = prevgreatest(arr,12)
prevsmall = prevsmallest(arr,12)

print(l)
print(d)
print(prev)
print(prevsmall)



















