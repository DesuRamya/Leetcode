class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c = 0
        p = 0
        prefix_map = {0:1}
        for i in nums:
            p+=i
            mod = p%k
            if mod<0:
                mod+=k
            if mod in prefix_map:
                c+=prefix_map[mod]
                prefix_map[mod]+=1
            else:
                prefix_map[mod] = 1
        return c