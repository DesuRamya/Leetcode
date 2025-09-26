class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i in range(len(nums2)):
            for j in range(i+1,len(nums2)):
                if nums2[i] < nums2[j]:
                    d[nums2[i]] = nums2[j]
                    break
            else:
                d[nums2[i]] = -1
        l = []
        for i in nums1:
            l.append(d[i])
        return l