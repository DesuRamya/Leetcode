class Solution:
    def printVertically(self, s: str) -> List[str]:
        l = s.split()
        res = []
        max_len = max(len(i) for i in l)
        for i in range(max_len):
            cur = ""
            for j in l:
                if i<len(j):
                    cur += j[i]
                else:
                    cur+=" "
            res.append(cur.rstrip())
        return res