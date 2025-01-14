class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        l1=[]
        l2=[0]*(n+1)
        c=0
        for i in range(n):
            l2[A[i]]+=1
            if l2[A[i]]==2:
                c+=1
            l2[B[i]]+=1
            if l2[B[i]]==2:
                c+=1
            l1.append(c)
        return l1