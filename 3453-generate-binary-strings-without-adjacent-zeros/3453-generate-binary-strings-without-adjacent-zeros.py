class Solution:
    def validStrings(self, n: int) -> List[str]:
        l=[]
        for i in range(1<<n):
            l.append(format(i,'0'+str(n)+'b'))
        # print(l)
        l1=[]
        for i in l:
            if '00' not in i:
                l1.append(i)
        return l1