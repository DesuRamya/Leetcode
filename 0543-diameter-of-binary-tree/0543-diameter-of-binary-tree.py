# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def Depth(root,res):
            if root is None:
                return 0
            d1=Depth(root.left,res)
            d2=Depth(root.right,res)
            res[0]=max(res[0],d1+d2)
            return 1+max(d1,d2)
        res=[0]
        Depth(root,res)
        return res[0]