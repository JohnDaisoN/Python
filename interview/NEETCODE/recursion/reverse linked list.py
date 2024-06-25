'''
here recursion phase starts

code is not important -
it is how ypur reach there

base case
subproblem

initial head - 1 - start at 1

1 -> 2 -> 3 ..

we ca reverse remainder list 

reverse only 1 node - last node bec

last node's next points to null

then when we return to the case where two last elements occur

now last node's next link can point to the previous node 

maybe???

we can only point next when we have that element

first - null<-3
then null<-2<-3

'''

if not head:
    return None
newHead = newHead
if head.next:
    newHead = self.reverseList(head.next)
    head.next.next = newHead

head.next = null