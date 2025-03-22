class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        l=sorted(prices)
        return money-(l[0]+l[1]) if l[0]+l[1]<=money else money