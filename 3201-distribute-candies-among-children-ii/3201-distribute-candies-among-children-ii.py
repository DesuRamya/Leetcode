class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def ways(n):
            if n<0:
                return 0
            return NCK(n+2,2)
        def NCK(n,k):
            res=1
            for i in range(1,k+1):
                res=res*(n-i+1)//i
            return res
        l=limit+1
        c1=ways(n-l)
        c2=ways(n-2*l)
        c3=ways(n-3*l)
        print(c1,c2,c3)
        return ways(n)-3*c1+3*c2-c3
        