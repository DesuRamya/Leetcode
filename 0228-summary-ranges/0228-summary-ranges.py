class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        s=0
        n=len(nums)
        l=[]
        if nums==[]:
            return []
        for i in range(1,n):
            if nums[i]!=nums[i-1]+1:
                if s+1==i:
                    l.append(str(nums[s]))
                else:
                    l.append(f"{nums[s]}->{nums[i-1]}")
                s=i
        if s == n - 1:
            l.append(str(nums[s]))
        else:
            l.append(f"{nums[s]}->{nums[n - 1]}")
        return l