class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ps=[0]*(n+1)
        for i in range(1,n+1):
            ps[i]=ps[i-1]+nums[i-1]
        dq=deque()
        res=float("inf")
        for i in range(n+1):
            while dq and ps[i]-ps[dq[0]]>=k:
                res=min(res,i-dq.popleft())
            while dq and ps[i]<=ps[dq[-1]]:
                dq.pop()
            dq.append(i)
            # print(dq)
        return -1 if res==float("inf") else res