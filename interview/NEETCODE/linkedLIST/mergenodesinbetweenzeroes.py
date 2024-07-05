
'''Topics
Companies
Hint
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]

        """
        a = head#this node to 
        # curr = head
        curr = a

        while a.next != None:
            

            # temp = ListNode()
            sumofnodes = 0
            while a.next.val != 0:
                sumofnodes += a.next.val
                a = a.next
            curr.val = sumofnodes
            # curr.next = temp
            a = a.next
            if a.next:
                curr.next = a.next
            else:
                curr.next = None
            curr = a.next


            # curr = a.
             
            # curr = a.next
        # head = head.next
        
        return head
'''
so thankfil to ramkowshik sir to make me believe that i could try out this medium linked
list problem on my own. i thought i wouldnt get it at a times - but managed to crack it out

but after completion i presume that this is actually a trivial problem and solution

it could be even recursively solved - tailr ecuesion extc
somehow the testcases passed - and solution got accespted

but runtime - like 3891 ms and memory around 200 mb - ammahhh - tc shouldbt be this high

maye there is some optimization possible

i will paste or describre neetcodesolution hereby


'''
'''
couple solutions

newlist

res = null

we create dummy node _-> next

we get a sum node - we append it to end

pointer always start at 0, keep going till we reach 0

my soltuon is similar and maybe same

cur = head
dummy = ListNode()
tail = dummy

while cur.next:
    nODE = listnode()
    while cur.next.val != 0:
        node.val += cur.next.val
        cur = cur.next
    tail.next = node
    tail = tail.next
    cur = cur.next


return dummy.next



INPLACE SOLUTION

did i dp this as well
i dont know


cur = head
while cur.next:
    node = cur = cur.next
    while cur.next.val != 0:
        node.val += cur.next.val
        cur = cur.next
    
    cur = cur.next
    node.next = cur.next
return head.next

'''

