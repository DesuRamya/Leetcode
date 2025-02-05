class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(nums):
            r,nr,tr=0,0,0
            for i in range(len(nums)):
                tr=max(r,nr)
                r=nr+nums[i]
                nr=tr
            return max(r,nr)
        n=len(nums)
        if n==1:
            return nums[0]
        x=rob1(nums[:n-1])
        y=rob1(nums[1:])
        return max(x,y)