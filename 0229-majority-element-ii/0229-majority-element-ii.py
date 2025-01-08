import sys
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[]
        c1,c2,e1,e2=0,0,0,0
        for i in range(len(nums)):
            cur=nums[i]
            if c1==0 and cur!=e2:
                e1=cur 
                c1+=1
            elif c2==0 and cur!=e1:
                e2=cur
                c2+=1
            elif cur==e1:
                c1+=1
            elif cur==e2:
                c2+=1
            else:
                c1-=1
                c2-=1
        l=[]
        c1, c2 = 0, 0
        for i in range(n):
            if nums[i] == e1:
                c1 += 1
            if nums[i] == e2:
                c2 += 1
        mini = n // 3
        if c1 > mini:
            l.append(e1)
        if c2 > mini:
            l.append(e2)
        return list(set(l))