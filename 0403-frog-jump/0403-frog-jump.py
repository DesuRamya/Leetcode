class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d={}
        for i in  stones:
            d[i]=set()
        d[0].add(1)
        for i in stones:
            for j in d[i]:
                r=i+j
                    # print(r)
                if r==stones[len(stones)-1]:
                    return True
                if r in d:
                    if j-1>0:
                        d[r].add(j-1)
                    d[r].add(j)
                    d[r].add(j+1)
        return False
                