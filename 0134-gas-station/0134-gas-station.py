class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        su,a,ind=0,0,0
        n=len(gas)
        for i in range(n):
            su+=gas[i]-cost[i]
            a+=gas[i]-cost[i]
            if a<0:
                a=0
                ind=i+1
        return ind if su>=0 else -1