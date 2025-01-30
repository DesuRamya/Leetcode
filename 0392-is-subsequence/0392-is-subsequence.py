class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a,b=0,0
        l1,l2=len(s),len(t)
        c=0
        if l1==0:
            return True
        while a<l1 and b<l2:
            if s[a]==t[b]:
                a+=1
                b+=1
                c+=1
            else:
                b+=1
        return True if c==l1  else False