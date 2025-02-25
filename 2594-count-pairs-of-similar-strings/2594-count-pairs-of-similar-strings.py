class Solution:
    def similarPairs(self, words: List[str]) -> int:
        d=defaultdict(int)
        for i in words:
            bits=0
            for j in i:
                bits|=(1<<(ord(j)-ord('a')))
            d[bits]+=1
        count=0
        for i in d.values():
            count+=(i*(i-1)//2)
        return count