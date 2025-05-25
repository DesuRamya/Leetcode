# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recurse(root,res):
            if root is None:
                return
            res.append(root.val)
            recurse(root.left,res)
            recurse(root.right,res)
        res=[]
        recurse(root,res)
        return res