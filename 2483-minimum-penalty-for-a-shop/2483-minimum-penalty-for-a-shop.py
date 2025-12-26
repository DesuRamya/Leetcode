class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cur=0
        for i in customers:
            if i == 'Y':
                cur += 1
        minPenalty = cur
        t = 0
        for i, ch in enumerate(customers):
            if ch == 'Y':
                cur-=1
            else:
                cur+=1
            if cur<minPenalty:
                t = i+1
                minPenalty = cur
        return t