class Solution:
    def clearStars(self, s: str) -> str:
        l=[[] for i in range(26)]
        arr=list(s)
        for i,c in enumerate(arr):
            if c!="*":
                l[ord(c)-ord("a")].append(i)
            else:
                for j in range(26):
                    if l[j]:
                        arr[l[j].pop()]="*"
                        break
        return "".join(c for c in arr if c!="*")