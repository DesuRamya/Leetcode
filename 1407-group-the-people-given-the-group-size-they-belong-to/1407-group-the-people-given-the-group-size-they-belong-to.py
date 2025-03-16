class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d={}
        ind=0
        for i in groupSizes:
            if i in d:
                d[i].append(ind)
            else:
                d[i]=[]
                d[i].append(ind)
            ind+=1
        l=[]
        s,e=0,0
        d=dict(sorted(d.items(),key=lambda x:x[0]))
        for i in d:
            k,v=i,d[i]
            for j in range(0,len(v),k):
                # sl=list(d[i][j:j+i])
                l.append(list(v[j:j+k]))
        return l
            