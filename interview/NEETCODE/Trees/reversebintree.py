# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
'''
def no explanati0n needed

reversingmeans just recursively looking at root , swappingleft and right values

i think that there wont be any problem if we invert right before left

just rmber to return root
and the     None case - whenno root
'''