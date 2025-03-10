class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        l=[ceil(dist[i]/speed[i]) for i in range(len(dist))]
        l=sorted(l)
        res=0
        i=0
        while i<len(l)  and l[i]>i:
                res+=1
                i+=1
        return res