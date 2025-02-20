class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        c=0
        while(l<r):
            c=max(c,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return c