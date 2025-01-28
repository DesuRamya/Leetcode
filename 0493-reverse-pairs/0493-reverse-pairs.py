class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums,l,mid,r):
            c,j=0,mid+1
            for i in range(l,mid+1):
                while j<=r and nums[i]>2*nums[j]:
                    j += 1
                c+= (j - (mid + 1))
            nl=[]
            i,j=l,mid+1
            while i<=mid and j<=r:
                if nums[i]<=nums[j]:
                    nl.append(nums[i])
                    i+=1
                else:
                    nl.append(nums[j])
                    j+=1
            while i<=mid:
                nl.append(nums[i])
                i+=1
            while j<=r:
                nl.append(nums[j])
                j+=1
            nums[l:r+1]=nl
            return c
        def MergeSort(nums,l,r):
            if l>=r:
                return 0
            mid=(r+l)//2
            left=MergeSort(nums,l,mid)
            right=MergeSort(nums,mid+1,r)
            c=merge(nums,l,mid,r)
            return c+left+right
        return MergeSort(nums,0,len(nums)-1)