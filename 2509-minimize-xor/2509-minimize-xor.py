class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bc1, bc2 = num1.bit_count(), num2.bit_count()
        if bc1 >= bc2:
            for i in range(bc1 - bc2):
                num1 = num1 & (num1 - 1)
        else:
            for i in range(bc2 - bc1):
                num1 = ~(~num1 & (~num1 - 1))
        return num1