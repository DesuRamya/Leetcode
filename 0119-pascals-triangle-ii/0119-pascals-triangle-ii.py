class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l=[[1]]
        for i in range(1,rowIndex+1):
            l1=[1]
            for j in range(1,i):
                l1.append(l[i-1][j-1]+l[i-1][j])
            if i>0:
                l1.append(1)
            l.append(l1)
        return l[rowIndex]