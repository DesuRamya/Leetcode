from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(num):
            count = Counter(str(num))
            return all(int(digit) == freq for digit, freq in count.items()) 
        
        n += 1
        while not is_balanced(n):
            n += 1
        return n