class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l,n=[],len(grid)
        for i in grid:
            for j in i:
                l.append(j)
        for i in range(1,(n*n)+1):
            if i not in l:
                x1=i
            if l.count(i)>1:
                x2=i
        return [x2,x1] 