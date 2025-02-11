class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l=sorted(skill)
        target=l[0]+l[-1]
        op=0
        n=len(l)
        for i in range(n//2):
            if l[i]+l[-i-1]!=target:
                return -1
            op+=(l[i]*l[-i-1])
        return op