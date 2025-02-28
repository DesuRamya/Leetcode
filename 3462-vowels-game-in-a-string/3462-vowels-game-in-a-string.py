class Solution:
    def doesAliceWin(self, s: str) -> bool:
        c=0
        l=['a','e','i','o','u']
        for i in s:
            if i in l:
                c+=1
        if  c==0:
            return False
        return True