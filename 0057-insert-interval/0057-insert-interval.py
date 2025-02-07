class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        l=[]
        for i in range(len(intervals)):
            if not l or intervals[i][0]>l[-1][1]:
                l.append(intervals[i])
            else:
                l[-1][1]=max(l[-1][1],intervals[i][1])
        return l
