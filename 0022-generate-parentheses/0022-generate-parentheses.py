class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lp,rp=0,0
        res=[]
        def fun(lp,rp,s):
            if len(s)==2*n:
                res.append(s)
                return
            if lp<n:
                fun(lp+1,rp,s+'(')
            if rp<lp:
                fun(lp,rp+1,s+')')
        fun(lp,rp,"")
        return res