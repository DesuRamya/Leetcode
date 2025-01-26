class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        prefix_sum=[0]*n
        for i in range(n):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
        n=len(prefix_sum)
        print(prefix_sum)
        for i in range(1,n):
            a=prefix_sum[i]
            b=prefix_sum[-1]-prefix_sum[i]
            print(a,b)
            if abs(a-b)%2==0:
                c+=1
        return c