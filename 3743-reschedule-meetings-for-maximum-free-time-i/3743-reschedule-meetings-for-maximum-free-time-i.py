class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        l,x=[],len(startTime)
        if startTime[0]!=0:
            l.append(startTime[0])
        else:
            l.append(0)
        for i in range(x-1):
            l.append(startTime[i+1]-endTime[i])
        if endTime[-1]!=eventTime:
            l.append(eventTime-endTime[-1])
        else:
            l.append(0)
        ms= 0
        cur=sum(l[:k+1])
        ms = cur
        for i in range(1, len(l) - k):
            cur=cur - l[i - 1] + l[i + k]
            ms = max(ms, cur)
        return ms