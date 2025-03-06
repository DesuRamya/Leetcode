class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefixSum=[]
        prefixSum.append(nums[0])
        avg=prefixSum[0]//1
        maxi=avg
        for i in range(1,len(nums)):
            prefixSum.append(prefixSum[i-1]+nums[i])
            avg=ceil(prefixSum[i]/(i+1))
            maxi=max(maxi,avg)
        return maxi