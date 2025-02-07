class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        m,c=0,0
        while l<=r:
            m=min(height[l],height[r])
            c=max(c,m*(r-l))
            if height[l]==m:
                l+=1
            else:
                r-=1
        return c