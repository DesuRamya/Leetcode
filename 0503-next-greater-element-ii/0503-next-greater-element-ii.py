class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        n = len(nums)
        res = [-1]*n
        for i in range(2*n-1,-1,-1):
            cur = nums[i%n]
            while st and st[-1]<=cur:
                st.pop()
            if i<n:
                res[i]=st[-1] if st else -1
            st.append(cur)
        return res