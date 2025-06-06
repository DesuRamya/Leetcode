class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        max_val=float("-inf")
        val=0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    val=(nums[i]-nums[j])*nums[k]
                    max_val=max(val,max_val)
        return max_val if max_val>0 else 0