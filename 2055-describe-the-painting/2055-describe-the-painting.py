class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        d={}
        for i in range(len(segments)):
            if segments[i][0] in d:
                d[segments[i][0]]+=segments[i][2]
            else:
                d[segments[i][0]]=segments[i][2]
            if segments[i][1] in d:
                d[segments[i][1]]-=segments[i][2]
            else:
                d[segments[i][1]]=-1*segments[i][2]
        prev,su=-1,0
        # d=sorted(d)
        print(d)
        res = {key: val for key, val in sorted(d.items(), key = lambda ele: ele[0])}
        l=[]
        for i in res:
            cur=i
            if prev!=-1 and su>0:
                l.append([prev,cur,su])
            su+=res[i]
            prev=cur     
        return l