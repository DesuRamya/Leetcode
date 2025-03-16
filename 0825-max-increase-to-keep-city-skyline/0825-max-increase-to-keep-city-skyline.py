class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rm=[float("-inf")]*len(grid)
        cm=[float("-inf")]*len(grid)
        for i in range(len(grid)):
            for j in range(len(grid)):
                rm[i]=max(rm[i],grid[i][j])
                cm[j]=max(cm[j],grid[i][j])
        s=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                s+=min(rm[i],cm[j])-grid[i][j]
        return s