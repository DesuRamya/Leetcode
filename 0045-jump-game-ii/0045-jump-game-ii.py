class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        m,l=0,0
        c=0
        for i in range(n):
            m=max(m,i+nums[i])
            if l==i:
                c+=1
                l=m
                if m>=n-1:
                    return c
        return 0
            
