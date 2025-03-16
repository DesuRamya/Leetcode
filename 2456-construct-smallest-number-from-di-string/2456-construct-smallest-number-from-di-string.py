class Solution:
    def smallestNumber(self, pattern: str) -> str:
        st,op=[],""
        ind=1
        for i in pattern:
            if i=="I":
                st.append(str(ind))
                while st:
                    op+=st.pop()
            else:
                st.append(str(ind))
            ind+=1
        st.append(str(ind))
        while st:
            op+=st.pop()
        return op
