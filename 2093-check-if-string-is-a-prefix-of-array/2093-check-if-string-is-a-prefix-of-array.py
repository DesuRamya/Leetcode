class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        r=''
        for i in words:
            if r+i==s:
                return True
            r=r+i
        return False