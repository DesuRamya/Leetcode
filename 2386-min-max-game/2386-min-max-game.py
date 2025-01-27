class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n=len(nums)
        arr=[0]*(n//2)
        if len(nums)==1:
            return nums[0]
        val=True
        for i in range(0,n//2):
            if val:
                arr[i]=min(nums[2*i+1],nums[2*i])
                val=False
            else:
                arr[i]=max(nums[2*i+1],nums[2*i])
                val=True
        return self.minMaxGame(arr)