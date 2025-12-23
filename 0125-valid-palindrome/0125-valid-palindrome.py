class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = ''
        for i in s:
            if i.isalnum():
                l+=i
        l = l.lower()
        return l==l[::-1]