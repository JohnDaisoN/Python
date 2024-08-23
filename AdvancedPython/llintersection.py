class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
def llintersection(list1,list2):
    newlisthead = None
    temp = None
    while list1 != None and list2 != None:
        if list1.data == list2.data:
            if newlisthead == None:
                newlisthead = ListNode(list1.data)
                temp = newlisthead
            else:
                temp.next = ListNode(list1.data)
                temp = temp.next
            list1 = list1.next
            list2 = list2.next
        elif list1.data < list2.data
        

