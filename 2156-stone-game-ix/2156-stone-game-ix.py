class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        l=[0,0,0]
        for i in stones:
            l[i%3]+=1
        if l[0]%2==0:
            return min(l[1],l[2])>0
        else:
            return abs(l[1]-l[2])>2