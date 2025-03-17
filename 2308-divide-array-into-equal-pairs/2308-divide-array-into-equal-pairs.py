from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d=Counter(nums)
        v=list(d.values())
        for i in v:
            if i%2!=0:
                return False
        return True