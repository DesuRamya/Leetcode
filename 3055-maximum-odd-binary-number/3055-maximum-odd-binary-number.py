class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        d1=s.count("1")
        d2=s.count("0")
        op="1"*(d1-1)+"0"*(d2)+"1"
        return op