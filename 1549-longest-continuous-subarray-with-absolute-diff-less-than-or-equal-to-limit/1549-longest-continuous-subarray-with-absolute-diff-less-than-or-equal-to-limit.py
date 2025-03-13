class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        d=SortedDict()
        l,max_len=0,0
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
            while d.peekitem(-1)[0]-d.peekitem(0)[0]>limit:
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    d.pop(nums[l])
                l+=1
            max_len=max(max_len,i-l+1)
        return max_len
