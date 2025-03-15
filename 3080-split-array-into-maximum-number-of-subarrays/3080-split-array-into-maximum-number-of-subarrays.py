from collections import Counter
class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        c,s=0,0
        for i in nums:
            if s==0:
                s=i
            else:
                s=s&i
            if s==0:
                c+=1
        return max(c,1)