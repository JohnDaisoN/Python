class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
    
def insertAtEnd(head,val):
    if not head:
        head = Node(val)
        return head
    else:
        temp = Node(val)
        a = head
        while a.next != None:
            a = a.next
        a.next = temp
        temp.prev = a
        return head

def insertAtBeginning(head,val):
    if not head:
        head = Node(val)
        return head
    else:
        temp = Node(val)
        head.prev = temp
        temp.next = head
        head = temp
        return head


        # head.next = temp
        # temp.next = None
head = None
head = insertAtEnd(head,4)
head = insertAtEnd(head,3)
head = insertAtEnd(head,1)
head = insertAtEnd(head,2)
head3 = head
while head3.next != None:
    print(f'{head3.val}--><--',end='')
    head3 = head3.next
print(head3.val)


