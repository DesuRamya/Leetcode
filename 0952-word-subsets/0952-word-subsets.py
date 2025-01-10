class Solution:
    def wordSubsets(self, w1: List[str], w2: List[str]) -> List[str]:
        def count(s1):
            ans=[0]*26
            for i in s1:
                ans[ord(i)-ord('a')]+=1
            return ans
        
        w2l=[0]*26
        for i in w2:
            for j,c in enumerate(count(i)):
                w2l[j]=max(w2l[j],c)
        res=[]
        for i in w1:
            if all(x>=y for x,y in zip(count(i),w2l)):
                res.append(i)
        return res