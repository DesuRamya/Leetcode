from sortedcontainers import SortedList
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        s1=SortedList(nums,key=lambda x:-x)
        su1=sum(s1)
        half=su1/2
        op=0
        while su1>half:
            p1=s1.pop(0)/2
            su1-=p1
            s1.add(p1)
            op+=1
        return op

            