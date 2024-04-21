class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row=len(grid)
        col=len(grid[0])
        rowone=[0]*row
        colone=[0]*col
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    rowone[i]+=1
                    colone[j]+=1
        # print(rowone)
        # print(colone)
        for ii in range(row):
            for jj in range(col):
                grid[ii][jj]=rowone[ii]+colone[jj]-(row-rowone[ii]+col-colone[jj])
        return grid            
        