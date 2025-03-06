class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f,e=float("inf"),float("inf")
        for i in nums:
            if i<=f:
                f=i
            elif i<=e:
                e=i
            else:
                return True
        return False