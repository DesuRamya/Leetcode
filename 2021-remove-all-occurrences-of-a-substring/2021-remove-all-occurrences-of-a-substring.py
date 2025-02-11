class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        def checkEqual(st,part,l2):
            return "".join(st[-l2:])==part
        st=[]
        l1,l2=len(s),len(part)
        for i in s:
            st.append(i)
            if len(st)>=l2 and checkEqual(st,part,l2):
                for _ in range(l2):
                    st.pop()
        return "".join(st)
