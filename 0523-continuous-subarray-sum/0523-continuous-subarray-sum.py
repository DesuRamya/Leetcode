class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        mod_seen={0:-1}
        ps=0
        for i in range(n):
            ps=(ps+nums[i])%k
            if ps in mod_seen:
                if i-mod_seen[ps]>1:
                    return True
            else:
                mod_seen[ps]=i
        return False