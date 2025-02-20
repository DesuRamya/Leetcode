class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s=set(nums)
        n=len(nums)
        ans=""
        def Check(cur):
            if (len(cur)==n):
                if cur not in s:
                    return cur
                return None
            for i in "01":
                ans=Check(cur+i)
                if ans:
                    return ans
            return None
        return Check("")
