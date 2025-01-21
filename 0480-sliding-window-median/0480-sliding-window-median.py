from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def balance():
            if len(low)>len(high)+1:
                high.add(low[-1])
                low.remove(low[-1])
            if len(low)<len(high):
                low.add(high[0])
                high.remove(high[0])
        low,high=SortedList(),SortedList()
        l=[]
        for i in range(len(nums)):
            if not low or nums[i]<=low[-1]:
                low.add(nums[i])
            else:
                high.add(nums[i])
            balance()
            if i>=k:
                if nums[i-k] in low:
                    low.remove(nums[i-k])
                else:
                    high.remove(nums[i-k])
                balance()
            if i>=k-1:
                if k%2==1:
                    l.append(low[-1])
                else:
                    l.append((low[-1]+high[0])/2)
        return l
