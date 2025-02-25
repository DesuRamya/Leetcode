class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefixSum=[]
        prefixSum.append(arr[0])
        for i in range(1,len(arr)):
            prefixSum.append(prefixSum[i-1]+arr[i])
        oc,ec,c=0,1,0
        for i in range(len(prefixSum)):
            if prefixSum[i]%2==1:
                c+=ec
                oc+=1
            else:
                ec+=1
                c+=oc
        return c%((10**9)+7)