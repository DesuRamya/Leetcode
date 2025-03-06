class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ol=0
        intervals=sorted(intervals, key=lambda x: x[1])
        print(intervals)
        e=intervals[0][1]
        s=intervals[0][0]
        for i in range(1,len(intervals)):
            # e=intervals[i-1][1]
            if intervals[i][0]>=e:
                e=intervals[i][1]
            else:
                ol+=1
        return ol