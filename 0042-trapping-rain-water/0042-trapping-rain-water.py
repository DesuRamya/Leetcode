class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l1,l2=[0]*n,[0]*n
        ma=height[0]
        l1[0]=height[0]
        l2[-1]=height[-1]
        for i in range(1,n):
            ma=max(ma,height[i])
            l1[i]=ma
        ma,su=height[-1],0
        for i in range(n-2,-1,-1):
            ma=max(ma,height[i])
            l2[i]=ma
        res=[]
        for i in range(n):
            res.append(min(l1[i],l2[i]))
        for i in range(n):
            su+=(res[i]-height[i])
        return su