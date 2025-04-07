class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        l,r=0,1
        sums=set()
        while r<len(nums):
            if nums[l]+nums[r] in sums:
                return True
            else:
                sums.add(nums[l]+nums[r])
            l+=1
            r+=1
        return False