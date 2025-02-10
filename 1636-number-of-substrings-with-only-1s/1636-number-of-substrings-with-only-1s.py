class Solution:
    def numSub(self, s: str) -> int:
        res=0
        c=0
        for i in s:
            if i=="1":
                c+=1
            else:
                res+=(c*(c+1)//2)
                c=0
        if c>0:
            res+=(c*(c+1)//2)
        return res%(10**9+7)