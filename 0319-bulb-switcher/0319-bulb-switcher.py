class Solution:
    def bulbSwitch(self, n: int) -> int:
        c=0
        for i in range(1,n+1):
            if i*i<=n:
                print(i)
                c+=1
            else:
                break
        return c