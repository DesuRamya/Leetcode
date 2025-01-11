class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        l=len(s)
        if l<k:
            return False
        if l==k:
            return True
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        for i in d.values():
            if i%2==1:
                c+=1
        return c<=k