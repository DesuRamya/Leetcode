class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n=len(s)
        op=""
        if n%2==0:
            for i in range(n//2):
                if s[i]<s[n-i-1]:
                    op+=s[i]
                else:
                    op+=s[n-i-1]
            op+=op[::-1]
        else:
            for i in range(n//2+1):
                if s[i]<s[n-i-1]:
                    op+=s[i]
                else:
                    op+=s[n-i-1]
            r=op[:n//2][::-1]
            op+=r
        return op