class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        l1=[0]
        for i in range(len(derived)):
            l1.append(l1[i]^derived[i])
        return l1[0]==l1[-1]