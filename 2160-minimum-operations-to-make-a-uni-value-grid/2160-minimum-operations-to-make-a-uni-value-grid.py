class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        l=[]

        for i in grid:
            for j in i:
                l.append(j)
        l=sorted(l)
        le=len(l)
        count=0
        median=l[(le//2)]
        print(median)
        for i in l:
            if i%x==median%x:
                count+=(abs(median-i)//x)
            else:
                return -1
        return count