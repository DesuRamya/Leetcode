class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for i in num:
            while st and st[-1]>i and k>0:
                st.pop()
                k-=1
            st.append(i)
        st=st[:-k] if k>0 else st
        s="".join(st).lstrip("0")
        return s if s else "0"