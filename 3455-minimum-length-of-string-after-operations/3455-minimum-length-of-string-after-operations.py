class Solution:
    def minimumLength(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        for i in d.values():   
            if i%2==0:
                c+=(i-2)
            else:
                c+=(i-1)
        return len(s)-c