class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st = []
        if len(nums)<3:
            return False
        min_array = [-1] *len(nums)
        min_array[0] = nums[0]
        for i in range(1,len(nums)):
            min_array[i] = min(min_array[i-1],nums[i])
        for i in range(len(min_array)-1,-1,-1):
            if nums[i] <= min_array[i]:
                continue
            while st and st[-1]<=min_array[i]:
                st.pop()
            if st and st[-1]<nums[i]:
                return True
            st.append(nums[i])
        return False