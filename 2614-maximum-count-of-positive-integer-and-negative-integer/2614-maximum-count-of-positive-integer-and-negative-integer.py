class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        nc,pc=0,0
        for i in nums:
            if i<0:
                nc+=1
            elif i>0:
                pc+=1
        return max(pc,nc)
