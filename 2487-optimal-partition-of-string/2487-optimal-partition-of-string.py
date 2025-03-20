class Solution:
    def partitionString(self, s: str) -> int:
        res,c="",0
        for i in s:
            if i in res:
                res=""
                res+=i
                c+=1    
                print(res,c)
            else:
                res+=i
        return c+1 if res else c