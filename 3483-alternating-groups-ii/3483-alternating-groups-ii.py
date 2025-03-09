class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n=len(colors)
        res=0
        c=1
        lc=colors[0]
        for i in range(1,n+k-1):
            ind=i%n
            if colors[ind]==lc:
                c=1
                lc=colors[ind]
                continue
            c+=1
            if c>=k:
                res+=1
            lc=colors[ind]
        return res