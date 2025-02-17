# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(root):
            if root==None:
                return 0
            leftHeight=checkHeight(root.left)
            rightHeight=checkHeight(root.right)
            if leftHeight==-1 or rightHeight==-1 or  abs(leftHeight-rightHeight)>1:
                return -1
            return max(leftHeight,rightHeight)+1
        if root==None:
            return  True
        return checkHeight(root)!=-1