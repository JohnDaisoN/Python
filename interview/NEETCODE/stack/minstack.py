#my solution went almost near to the answer yet so far
import math
class MinStack:

    def __init__(self):
        self.array = []
        self.ma = math.inf

    def push(self, val: int) -> None:
        self.array.append(val)
        if val < self.ma:
            self.ma = val
        

    def pop(self) -> None:
        element = self.array.pop()
        return element
        

    def top(self) -> int:
        
            return self.array[-1]
        
        

    def getMin(self) -> int:
        return self.ma
        
'''
my fault is that i thought the minimum value will be always the same but i didnt consider what to do when we pop that minvalue

neetcode

workaround is maintaining a new stack which stores the minimum at each position, like at index 0 , min in both stacks same , but gradually they vary - like when we do add 
1, 2, 0



'''

# key - implement it in 0(1) time not 0(1) space - it is a hint as we can init any number of data structures - hence the 2 stacks


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
