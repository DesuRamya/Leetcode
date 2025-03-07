class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d=Counter(nums)
        if 1 in  d.values():
            return -1
        else:
            s=0
            l=list(d.values())
            for i in l:
                if i%3==0:
                    s+=i//3
                    i=0
                if i%3==1 or i%3==2:
                    s+=(i//3)+1
                    i=0
                if i%2==0:
                    s+=(i//2)
                    i=0
            return s