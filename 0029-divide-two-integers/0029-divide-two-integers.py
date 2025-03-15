class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if trunc(dividend/divisor)>(2**31)-1:
            return (2**31)-1
        elif trunc(dividend/divisor)<-1*(2**31):
            return -1*(2**31)
        else:
            return trunc(dividend/divisor)