from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1=Counter(s1)
        d2=Counter()
        k1,k2=len(s1),len(s2)
        if k1>k2:
            return False
        for i in range(k1):
            d2[s2[i]]+=1
        if d1==d2:
            return True
        for i in range(k1, k2):
            d2[s2[i]] += 1
            d2[s2[i - k1]] -= 1
            if d2[s2[i - k1]] == 0:
                del d2[s2[i - k1]]
            if d1 == d2:
                return True
        return False