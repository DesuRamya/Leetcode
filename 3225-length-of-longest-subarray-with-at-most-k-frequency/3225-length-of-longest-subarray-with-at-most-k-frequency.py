class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l,r=0,0
        ma=-1
        d={}
        while r<len(nums):
            if nums[r] in d:
                d[nums[r]]+=1
            else:
                d[nums[r]]=1
            while d[nums[r]]>k:
                d[nums[l]]-=1
                l+=1
            ma=max(ma,r-l+1)
            r+=1
        return ma
