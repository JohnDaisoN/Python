import math
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None, length=None):
#         self.length += 1
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        
        def tree_len( node):
            if node is None:
                return 0
            else:
                return 1 + max(tree_len(node.right),tree_len(node.left))# here lies important recursive solution easy to understand but takes time to know logica
            

        print(tree_len(root))
        if root:
            if tree_len(root) == 1:
                return 1
            else:
                a = tree_len(root)
                return a
        else:
            return 0
        


        """
        :type root: TreeNode
        :rtype: int
        """
        