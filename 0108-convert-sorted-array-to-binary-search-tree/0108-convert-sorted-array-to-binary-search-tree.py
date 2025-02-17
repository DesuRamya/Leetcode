# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def findTree(left,right,nums):
            if left>right:
                return None
            mid=(left+right)//2
            n=TreeNode(nums[mid])
            n.left=findTree(left,mid-1,nums)
            n.right=findTree(mid+1,right,nums)
            return n
        left,right=0,len(nums)-1
        return findTree(left,right,nums)