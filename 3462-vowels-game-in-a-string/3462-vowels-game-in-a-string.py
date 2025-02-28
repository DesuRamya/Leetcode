class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # c=0
        c=s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')
        # l=['a','e','i','o','u']
        # for i in s:
        #     if i in l:
        #         c+=1
        if  c==0:
            return False
        return True