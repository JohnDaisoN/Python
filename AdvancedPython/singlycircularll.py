class Node:
    def __init__(self,val):
        self.val = val
        self.next = self
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
        temp.next = head
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
        temp.next = head
        temp = head
        return head

# head = None
# head = InsertAtEnd(head,4)
# head = InsertAtEnd(head,3)
# head = InsertAtEnd(head,1)
# head = InsertAtEnd(head,2)
# head3 = head
# while head3.next != head:
#     print(f'{head3.val}--><--',end='')
#     print(f'the value of node is {head3.val} ,its next element is {head3.next.val}')
#     head3 = head3.next
# print(f'the value of node is {head3.val} ,its next element is {head3.next.val}')

head1 = None
head1 = InsertAtBeginning(head1,4)
head1 = InsertAtBeginning(head1,3)
head1 = InsertAtBeginning(head1,1)
head1 = InsertAtBeginning(head1,2)
head3 = head1
while head3.next != head1:
    print(f'{head3.val}--><--',end='')
    print(f'the value of node is {head3.val} ,its next element is {head3.next.val}')
    head3 = head3.next
print(f'the value of node is {head3.val} ,its next element is {head3.next.val}')



        