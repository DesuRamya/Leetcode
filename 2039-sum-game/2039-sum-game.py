class Solution:
    def sumGame(self, num: str) -> bool:
        sl,sr,ql,qr=0,0,0,0
        for i in range(len(num)//2):
            if num[i]=="?":
                ql+=1
            else:
                sl+=int(num[i])
        for i in range(len(num)//2,len(num)):
            if num[i]=="?":
                qr+=1
            else:
                sr+=int(num[i])
        ans1=(ql+qr)%2==1
        ans2=(sl-sr)!=9*(qr-ql)//2
        return ans1 or ans2