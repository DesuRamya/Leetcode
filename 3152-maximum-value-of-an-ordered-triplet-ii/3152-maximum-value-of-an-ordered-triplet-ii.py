class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res=a=b=0
        for i in nums:
            res=max(res,b*i)
            a=max(a,i)
            b=max(b,a-i)
        return res