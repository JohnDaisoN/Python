'''

Code
Testcase
Test Result
Test Result
1038. Binary Search Tree to Greater Sum Tree
Medium
Topics
Companies
Hint
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
#inorder traversal in reverse order
#go to right subtree - then root - then left 
#because the first node to calculate sum would be leaf nodes of rightmost subtree#then 
#work our way upwards - update root - then left subtree

#dfs

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.carry = 0
        def dfs(node):
            if not node: return#very easy code - this is how you dfs to find rightmost node
            dfs(node.right)#recurse till rightmost leaf found
            self.carry += node.val#rightmost node value first updated and then that added to carry
            node.val = self.carry
            dfs(node.left)#after the right is uodtaed , left is checked - go till rightmost of that left subtree if present and fill values from botoom again

        dfs(root)
        return root
