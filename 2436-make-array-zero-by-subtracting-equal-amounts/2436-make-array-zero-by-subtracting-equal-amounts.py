from collections import Counter
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d=Counter(nums)
        if 0 in nums:
            return len(d)-1
        return len(d)