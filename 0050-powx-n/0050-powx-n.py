class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1.0
        n1=n
        if n1<0:
            n1=-1*n1
        while n1:
            if n1%2==1:
                res=res*x
                n1=n1-1
            else:
                x=x*x
                n1=n1//2
        if n<0:
            res=1.0/res
        return res