class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def backtrack(ini,cur,nums,n):
            res.append(cur[:])
            for i in range(ini,n):
                cur.append(nums[i])
                backtrack(i+1,cur,nums,n)
                cur.pop()
        backtrack(0,[],nums,n)
        return res