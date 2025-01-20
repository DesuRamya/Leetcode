from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d=Counter(nums)
        cnt=0
        for i in d:
            if i+1 in d: 
                cnt=max(cnt,d[i]+d[i+1])
        return cnt