class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=len(fruits)
        l=[False]*n
        for i in range(n):
            for j in range(n):
                # print(j)
                if fruits[i]<=baskets[j] and l[j]==False: 
                    l[j]=True
                    break
        return l.count(False)