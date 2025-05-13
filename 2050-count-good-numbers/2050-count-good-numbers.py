class Solution:
    def countGoodNumbers(self, n: int) -> int:
        n1=n//2 if n%2==0 else (n//2)+1
        n2=n//2
        p1=pow(5,n1,10**9+7)
        p2=pow(4,n2,10**9+7)
        return (p1*p2)%(10**9+7)