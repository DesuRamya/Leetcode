class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)-2):
            if nums[i]==0:
                nums[i]=1 
                nums[i+1]=1 if nums[i+1]==0 else 0
                nums[i+2]=1 if nums[i+2]==0 else 0
                c+=1
        return c if nums==[1]*len(nums) else -1