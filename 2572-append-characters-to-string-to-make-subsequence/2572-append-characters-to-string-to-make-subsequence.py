class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i,j=0,0
        charCount=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
                charCount+=1
            else:
                i+=1
        # print(charCount,i,j)
        return len(t)-charCount