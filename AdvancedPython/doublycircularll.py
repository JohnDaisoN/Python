class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
def InsertAtEnd(head,val):
    if not head:
        head = Node(val)
        return head
    else:
        temp = Node(val)
        a = head
        while a.next != head:
            a = a.next
        a.next = temp
        temp.prev = a
        temp.next = head
        head.prev = temp
        return head
def InsertAtBeginning(head,val):
    if not head:
        head = Node(val)
        return head
    else:
        a = head
        temp = Node(val)
        while a.next != head:
            a = a.next
        a.next = temp
        temp.prev = a
        temp.next = head
        head.prev = temp
        return head

head = None
head = InsertAtEnd(head,4)
head = InsertAtEnd(head,3)
head = InsertAtEnd(head,1)
head = InsertAtEnd(head,2)
head3 = head
while head3.next != None:
    print(f'{head3.val}--><--',end='')
    head3 = head3.next
print(head3.val)



