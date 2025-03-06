class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        d={0:0,1:0,2:0}
        for i in stones:
            if i%3==0:
                d[0]+=1
            elif i%3==1:
                d[1]+=1
            else:
                d[2]+=1
        if d[0]%2==0:
            return min(d[1],d[2])>0
        else:
            return abs(d[1]-d[2])>2