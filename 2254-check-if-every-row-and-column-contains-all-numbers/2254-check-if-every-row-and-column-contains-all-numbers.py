class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        a=[i for i in range(1,len(matrix)+1)]
        for i in range(len(matrix)):
            s=sorted(matrix[i])
            if s!=a:
                return False
        n=0
        while(n<len(matrix)):
            b=[]
            for i in matrix:
                b.append(i[n])
            if sorted(b)!=a:
                return False
            n+=1
        return True