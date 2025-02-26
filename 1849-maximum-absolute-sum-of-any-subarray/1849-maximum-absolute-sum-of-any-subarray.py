class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        minPrefixSum=0
        maxPrefixSum=0
        prefixSum=0
        for i in nums:
            prefixSum+=i
            minPrefixSum=min(minPrefixSum,prefixSum)
            maxPrefixSum=max(maxPrefixSum,prefixSum)
        return maxPrefixSum-minPrefixSum
