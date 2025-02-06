class Solution:
    def hIndex(self, nums: List[int]) -> int:
        n=len(nums)
        o=0
        nums1=sorted(nums,reverse=True)
        for i in range(n):
            print("op")
            if nums1[i]>=i+1:
                o=i+1
        if nums==[0]:
            return 0
        if n==1:
            return 1
        return o