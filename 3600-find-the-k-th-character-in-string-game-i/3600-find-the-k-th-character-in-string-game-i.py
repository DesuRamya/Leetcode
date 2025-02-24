class Solution:
    def kthCharacter(self, k: int) -> str:
        c=(k-1).bit_count()%26
        return chr(97+c)
