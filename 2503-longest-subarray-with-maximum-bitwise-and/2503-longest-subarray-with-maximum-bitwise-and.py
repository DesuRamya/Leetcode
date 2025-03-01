class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi=max(nums)
        maxlen,c=0,0
        for i in range(len(nums)):
            if nums[i]==maxi:
                c+=1
                maxlen=max(c,maxlen)
            else:
                c=0
        return maxlen
