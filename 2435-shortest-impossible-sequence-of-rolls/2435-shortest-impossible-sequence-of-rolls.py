class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        se=set()
        ans=1
        for i in rolls:
            se.add(i)
            if len(se)==k:
                ans+=1
                se=set()
        return ans