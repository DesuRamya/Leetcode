class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n=len(nums)
        arr=[0]*(n//2)
        if len(nums)==1:
            return nums[0]
        for i in range(0,n//2):
            if i%2==0:
                arr[i]=min(nums[2*i+1],nums[2*i])
            else:
                arr[i]=max(nums[2*i+1],nums[2*i])
        return self.minMaxGame(arr)