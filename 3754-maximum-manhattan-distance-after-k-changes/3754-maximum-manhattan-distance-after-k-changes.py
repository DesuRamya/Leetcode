class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def getMax(st,x,y,k):
            maxii=0
            for i in range(len(s)):
                if s[i]=='N' and st[0]=='S' and k!=0 :
                    y-=1
                    k-=1
                elif s[i]=='N':
                    y+=1
                if s[i]=='S' and st[0]=='N' and k!=0:
                    y+=1
                    k-=1
                elif s[i]=='S':
                    y-=1
                if s[i]=='E' and st[1]=='W' and k!=0 :
                    x-=1
                    k-=1
                elif s[i]=='E':
                    x+=1
                if s[i]=='W' and st[1]=='E' and k!=0 :
                    x+=1
                    k-=1
                elif s[i]=='W':
                    x-=1
                maxii=max(maxii,abs(x)+abs(y))
            return maxii
        maxi=0
        maxi=max(maxi,getMax('NE',0,0,k),getMax('NW',0,0,k),getMax('SE',0,0,k),getMax('SW',0,0,k))
        return maxi