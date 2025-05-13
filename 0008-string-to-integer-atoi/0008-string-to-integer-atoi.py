class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip(" ")
        if not s:
            return 0
        res=""
        sign=False
        i=0
        if s[i] in ["+","-"]:
            if s[i]=="-":
                sign=True
            i+=1
        while i<len(s) and s[i].isdigit():
            res+=s[i]
            i+=1
        if not res:
            return 0
        res=int(res)
        if sign:
            res=-res
        if res<(-2)**31:
            return (-2)**31
        if res>2**31-1:
            return 2**31-1
        return res