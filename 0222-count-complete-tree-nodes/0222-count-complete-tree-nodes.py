# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.c=0
        def count(root):
            if root is None:
                return 
            self.c+=1
            count(root.left)
            count(root.right)
        
        if root is None:
            return 0
        count(root)
        return self.c