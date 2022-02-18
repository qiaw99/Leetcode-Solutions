class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0
        for i in range(len(grid)):
            if(grid[i][-1] >= 0):
                pass
            else:
                for j in range(len(grid[i])):
                    if(grid[i][-(j)] < 0):
                        counter += 1
        return counter
        