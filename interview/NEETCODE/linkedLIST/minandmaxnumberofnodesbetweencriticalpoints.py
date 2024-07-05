# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].'''


class Solution(object):

    '''
   i did the direct direct direct approach
    '''
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        a = head#alwaysd store head in other pointer, but in this case
        #i dont think it is necedsary bcuz we are returning array not hea
        # b = head
        index = 0#keep track of index or position of the valid critical point
        indarray = []#array to store indices of criticsalpoints
        result = []

        while a.next.next != None:#this is because we are checking only till second last node 
            #bcuz last node and first node will never be critical pointe ]
            #qaccording to definition given
            index += 1#update index for current value
            if a.val < a.next.val > a.next.next.val:#conditin formed based on definition
                indarray.append(index)
            elif a.val > a.next.val < a.next.next.val:
                indarray.append(index)
            a = a.next
            # b = b.next

        # print(indarray)
        if len(indarray)>1:
            #even if len == 1: we have to return -1,-1 bcuz there are no other critical nodes to 
            #form no: of nodes or something
            indarray.sort()#sorting is optional
            maxdifference = indarray[-1] - indarray[0]#or can be done like max(indarray)-min(indarray)
            i = 0
            mindifference = float('inf')
            for j in range(1,len(indarray)):#basic sliding pointers for min difference
                mindifference = min(mindifference,abs(indarray[i]-indarray[j]))
                i += 1
            result.append(mindifference)
            result.append(maxdifference)
       
        else:
            result = [-1,-1]
        return result