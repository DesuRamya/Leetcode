class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def Seive(n):
            Primes=[i for i in range(n+1)]
            i=2
            while (i*i<=n):
                if Primes[i]==i:
                    j=i*i
                    while(j<=n):
                        if Primes[j]==j:
                            Primes[j]=i
                        j+=i
                i+=1
            return Primes
        spf=Seive(right+1)
        l=[]
        for i in range(left,right+1):
            if spf[i]==i:
                l.append(spf[i])
        mini=float("inf")
        # print(l)
        if 1 in l:
            l.pop(0)
        l1=[]
        for i in range(len(l)-1):
            if mini>l[i+1]-l[i]:
                if len(l1)==2:
                    l1.pop()
                    l1.pop()
                mini=l[i+1]-l[i]
                l1.append(l[i])
                l1.append(l[i+1])
        return l1 if len(l1)>0 else [-1,-1]
