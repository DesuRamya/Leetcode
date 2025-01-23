class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        l,r=0,0
        ma=-1
        d={}
        while r<len(nums):
            if nums[r] in d:
                d[nums[r]]+=1
            else:
                d[nums[r]]=1
            while l<r and len(d)>2:
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    x=d.pop(nums[l])
                l+=1
            ma=max(ma,r-l+1)
            r+=1
        return ma