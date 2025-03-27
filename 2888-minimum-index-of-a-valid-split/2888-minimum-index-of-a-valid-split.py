class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n=len(nums)
        d1,d2=defaultdict(int),defaultdict(int)
        for i in nums:
            d2[i]+=1
        for i in range(n):
            ind=nums[i]
            d2[ind]-=1
            d1[ind]+=1
            if d1[ind]*2>i+1 and d2[ind]*2>n-i-1:
                return i
        return -1