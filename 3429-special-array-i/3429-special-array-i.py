class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l=[]
        for i in nums:
            if l: 
                if l[-1]!=i%2:
                    l.append(i%2)
                else:
                    return False
            else:
                l.append(i%2)
        return True