class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        d,n=k*2+1,len(nums)
        l=[-1]*k
        j1,j2=0,0
        su=sum(nums[:d])
        l.append(su//d)
        if k>=n or 2*k+1>n:
            return [-1]*n
        for i in range(k,n-k):
            if i+k+1<n:
                su+=nums[i+k+1]-nums[i-k]
                l.append(su//d)
        for i in range(k):
            l.append(-1)
        return l