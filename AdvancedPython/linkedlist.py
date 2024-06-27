class Node:
    
    def __init__(self,val):
        # self.start = None
        

        self.val = val
        self.next = None
def AddNode(head,val):
    if not head:
        head = Node(val)
        return head
    else:
        temp = Node(val)
        temp.next = head
        head = temp
        return head
def AddAtEnd(head,val):
    if not head:
        head = Node(val)
        return head
    else:
        temp = Node(val)
        a = head
        while a.next != None:
            a = a.next
        a.next = temp
        
        return head

def findmiddle(head):
    l = head
    pos = 1
    while l.next != None:
        l = l.next
        pos += 1
    a = head
    i = 0
    while i < pos//2:
        a = a.next
        i += 1
    return a.val

    '''
   fast and slow pointers can be used to find middle element hen fast goes twice as fast as slow pointer
    '''

def deletemiddle(head):
    l = head
    pos = 1#head is at position 1 a
    while l.next != None:
        l = l.next
        pos += 1#find length of list
    a = head
    i = 1
    while i < pos//2:#finding element just before middle positon
        a = a.next
        i += 1
    a.next = a.next.next#connect links between before and after element of mid
    return a
    



head = None
head =AddAtEnd(head,1)
head = AddAtEnd(head,3)
head = AddAtEnd(head,5)
# head = AddAtEnd(head,2)

value = findmiddle(head)
print(value)
head = deletemiddle(head)
a = head
while a.next != None:
    print(f'{a.val}-->',end='')
    a = a.next
print(a.val)


# start = A






# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)

# a.next = b
# b.next = c
# c.next = d

# start = a
# while a.next != None:
#     print(f'{a.val}-->',end='')
#     a = a.next
# print(a.val)

    

        