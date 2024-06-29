# class stackusinglinkedlist:

#     class Node:
#         def __init__(self,val):
#         # self.start = None
        

#             self.val = val
#             self.next = None
#     def __init__(self):
        
#         self.stack = self.Node()
# def push(stack,val):
#     if not stack:
#         stack = stackusinglinkedlist()
#         s = stack.stack(val)
#         return s
#     else:
#         temp = stackusinglinkedlist()
#         t = temp.stack(val)
#         t.next = s
#         t = s
#         return s

# def pop(stack):
#     if stack:

class Node:
    def __init__(self,data):
#         # self.start = None
        

            self.data = data
            self.next = None
class susingl:
    def push(self,data,head):
        if not head:
            head = Node(data)
            return head
        else:
            newNode = Node(data)
            newNode.next = head
            head = newNode
            return head

    def pop(self,head):
        head = head.next
        return head.data

    def display(self,head):
        while head!= None:
            print(head.data)
            head = head.next
head = None
sl = susingl()
head= sl.push(1,head)
head= sl.push(2,head)
head= sl.push(3,head)
head= sl.push(4,head)

sl.display(head)








