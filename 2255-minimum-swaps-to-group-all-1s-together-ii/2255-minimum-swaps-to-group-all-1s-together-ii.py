class Solution:
    def minSwaps(self, arr: List[int]) -> int:
        n=len(arr)
        oc=0
        for i in arr:
            if i==1:
                oc+=1
        zc=arr[:oc].count(0)
        mini=zc
        for i in range(oc,n+oc):
            if arr[i-oc]==0:
                zc-=1
            if arr[i%n]==0:
                zc+=1
            mini=min(zc,mini)
        return mini if oc!=0 else 0