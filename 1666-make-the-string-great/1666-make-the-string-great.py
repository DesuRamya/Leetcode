class Solution:
    def makeGood(self, s: str) -> str:
        l = []
        l.append(s[0])
        for i in range(1,len(s)):
            if l  and abs(ord(l[-1]) - ord(s[i]))==32:
                l.pop(-1)
            else:
                l.append(s[i])
        return ''.join(l)