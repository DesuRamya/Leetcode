class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1/n if n<2 else 0.5