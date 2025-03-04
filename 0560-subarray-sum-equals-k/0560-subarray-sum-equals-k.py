class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum=[]
        prefixSum.append(nums[0])
        for i in range(1,len(nums)):
            prefixSum.append(prefixSum[i-1]+nums[i])
        d,res={},0
        # d[0]=1
        for i in range(len(nums)):
            if prefixSum[i] == k:
                res+=1
            if prefixSum[i]-k in d:
                res+=d[prefixSum[i]-k]
            if prefixSum[i] in d:
                d[prefixSum[i]]+=1
            else:
                d[prefixSum[i]]=1
        # print(d)
        return res