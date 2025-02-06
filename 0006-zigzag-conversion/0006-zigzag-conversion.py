class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        l=['']*numRows
        step,c=-1,0
        for i in s:
            l[c]+=i
            if c==0 or c==numRows-1:
                step=-step
            c+=step
        return ''.join(l)