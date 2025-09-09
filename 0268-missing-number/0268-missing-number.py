class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums :
            return 0
        n=len(nums)
        sumN = n*(n+1)//2
        sumNums = sum(nums)
        if sumN == sumNums :
            return n+1 
        return sumN - sumNums 