class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        l=sorted(nums)
        i,j,l1=0,len(nums)-1,[]
        while i<j:
            l1.append(l[i]+l[j])
            i+=1
            j-=1
        return max(l1)