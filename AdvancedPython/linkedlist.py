class Node:
    
    def __init__(self,val):
        # self.start = None
        

        self.val = val
        self.next = None

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)

A.next = B
B.next = C
C.next = D
D.next = E
E.next = C
# slow != fast

def cycledetection(head):
    slow = head
    fast = head.next

    while fast != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False

# variable = cycledetection(A)
# if variable == True: 
#     print('true')
# else:
#     print('False')



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

# def findmiddle(head):
#     l = head
#     pos = 1
#     while l.next != None:
#         l = l.next
#         pos += 1
#     a = head
#     i = 0
#     while i < pos//2:
#         a = a.next
#         i += 1
#     return a.val

    '''
   fast and slow pointers can be used to find middle element hen fast goes twice as fast as slow pointer
    '''

# def deletemiddle(head):
#     l = head
#     pos = 1#head is at position 1 a
#     while l.next != None:
#         l = l.next
#         pos += 1#find length of list
#     a = head
#     i = 1
#     while i < pos//2:#finding element just before middle positon
#         a = a.next
#         i += 1
#     a.next = a.next.next#connect links between before and after element of mid
#     return a
def deleteatkth(head,k):#for k th node - just find k th loop , but from back - we use length of ll - k  th position
    #aqnd do a.next = a.next.nex
    l = head
    pos = 1#head is at position 1 a
    while l.next != None:
        l = l.next
        pos += 1#find length of list
    a = head
    i = 1
    while i < pos-k:#finding element just before middle positon
        a = a.next
        i += 1
    a.next = a.next.next#connect links between before and after element of mid
    return head

def reversell(head):
    if not head:
        return None
    NewNode = head
    if head.next:
        NewNode = reversell(head.next)
        head.next.next = head
    head.next = None
    return NewNode
def reversell(head,k,i):
    if not head:
        return None
    NewNode = head
    if i <= 3:
        if head.next:
        
            
            NewNode = reversell(head.next,k,i+1)
    # i = 1
    # while i <= 3:
            
            head.next.next = head
            head.next = None
    # i = 0
    head.next = None        
    # head = NewNode.next    # head.next = 
    # reversell(head,k,0)
    return NewNode

def removeduplicates(head):
    if not head:
        return None
    if not head.next:
        return head
    
    a = head
    b = head.next
    while b != None:
        if a.val == b.val:
            b = b.next
        else:
            a.next = b
            a = b
            b = b.next

    return head

def removeduplicatesfromunsorted(head):
    if not head:
        return None
    if not head.next:
        return head
    
    a = head
    d = set()
    d.add(a.val)#this is done because first element will anyways be present as a new element
    #and we can start looking from a.next element
    
    while a.next != None:
        if a.next.val in d:
            a.next = a.next.next
            #current pointer need not incremented because the new link might point to a duplicate

            # b.next = a.next
        else:
            d.add(a.val)
            a = a.next#we should update the current only when the adjacent elements are newly found
           
            
            # a.next = b
            # a = b
            # b = b.next

    return head

            
            # d = b
            # b = d.next
            
            
            # if b.val > c.val:
            #     b.next = c.next
            #     c.next = b
            #     b = a.next.next
                

            # b.next = c
            # c = b
            # b = a.next.next
            

        # head = c

        # a = b
        # b = b.next 

    # return c
def zeroonetwo(head):
    c0 = 0
    c1 = 0
    c2 = 0

    temp = head
    while(temp!=None):
        if temp.val == 0:
            c0 += 1
        elif temp.val == 1:
            c1 += 1
        else:
            c2 += 1
        temp = temp.next
    temp1 = head
    while temp1!= None:
        if c0 != 0:
            temp1.val = 0
            c0 -= 1
        elif c1 != 0:
            temp1.val = 1
            c1 -= 1
        elif c2 != 0:
            temp1.val = 2
            c2 -= 1
        temp1 = temp1.next

    return head



        







    



# head = None
# head =AddAtEnd(head,12)
# head = AddAtEnd(head,42)
head = AddAtEnd(head,12)
# head = AddAtEnd(head,8)
# head = AddAtEnd(head,51)
# head = AddAtEnd(head,42)
# head = AddAtEnd(head,8)
# # head = AddAtEnd(head,55)
# # head = AddAtEnd(head,66)
# a = head
# while a.next != None:
#     print(f'{a.val}-->',end='')
#     a = a.next
# print(a.val)
# head = removeduplicatesfromunsorted(head)

# # head = deleteatkth(head,4)

# # head = AddAtEnd(head,2)

# # value = findmiddle(head)
# # print(value)
# # head = deletemiddle(head)
# b = head
# while b.next != None:
#     print(f'{b.val}-->',end='')
#     b = b.next
# print(b.val)


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

# def mergewithoutextrall(head1,head2):
#     a = head1
#     b = head2
#     ptr = None
#     # c = head1
   
#     if a.val > b.val:
#             # if b.val > c.val:
#             #     c.next = b
#         b.next = a
#         ptr = b
#             # else:
#             #     b.next = c

            
            
            
#             # a = a.next
#     else:
#         a.next = b
#         ptr = a
#     if ptr.next == a:
#         node = head2.next
#         while node != None:
#             if node.val > ptr.next.val:
#                 ptr = ptr.next
#             else:
#                 c.next = b
            
#             b.next = a
#     else:
#         c = head1.next
#         if c.val > a.val:
#             a = a.next
#         else:
#             c.next = a
#             a.next = b







    

        
            # else:
            #     b.next = c

            
            
            
            
            
            # if b.val > c.val:


            # b = b.next
    # return c

head1 = None
head1 =AddAtEnd(head1,1)
head1 = AddAtEnd(head1,2)
head1 = AddAtEnd(head1,13)
head1 = AddAtEnd(head1,27)
head2 = None
head2 = AddAtEnd(head2,11)
head2 = AddAtEnd(head2,22)
head2 = AddAtEnd(head2,33)
head2 = AddAtEnd(head2,44)
head3 = mergewithoutextrall(head1,head2)
while head3.next != None:
    print(f'{head3.val}-->',end='')
    head3 = head3.next
print(head3.val)



    

    

        