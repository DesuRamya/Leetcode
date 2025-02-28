class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        ans=0
        for i in range(n):
            ans=ans|nums[i]
        print(1<<(n-1))
        return ans*(1<<(n-1))