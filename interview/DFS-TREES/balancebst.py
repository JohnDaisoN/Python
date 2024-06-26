# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
itsd like creating an avl tree to be honest
its muche asirr on pen and paper

the hints are like

first do inorder traversal to get a sorted array
then do bsearch on the array, get the node
'''
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.array = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            self.array.append(root.val)
            inorder(root.right)
        inorder(root)#my inorder logic is pakka - ig, because output is sorted array and no None values
        sup = []

        def balance(array,l,r):#balance logic is going t osme recursive limit exceeded
            # l = 0
            # r = len(self.array)-1
            while l <= r:
                mid = l + ((r-l) // 2)
                
                balance(array,0,mid-1)
                sup.append(array[mid])
                balance(array,mid+1,len(self.array)-1)

            return sup

        balance(self.array,l=0,r=len(self.array)-1)

'''
problem

so basicallly - i thoight of 90% correct solution

just thew balancing part of the recursion

i should have specified 



'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def in_order_traversal(node):
            if not node:
                return []

            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)

        def build_balanced_bst(elements):
            if not elements:#return anONE CONDITION
                return None
            mid = len(elements) // 2#here no need l ,r just mid part is enough i think
            node = TreeNode(elements[mid])#here a node is created to store mid element
            node.left = build_balanced_bst(elements[:mid])
            node.right = build_balanced_bst(elements[mid + 1:])
            return node

        sorted_elements = in_order_traversal(root)
        return build_balanced_bst(sorted_elements)


        
        

        
        

        