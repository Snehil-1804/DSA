class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        col=len(matrix[0])
        rowtrack=[0]*row
        coltrack=[0]*col
        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j]==0:
                    rowtrack[i]=-1
                    coltrack[j]=-1
        for i in range(0,row):
            for j in range(0,col):
                if rowtrack[i]==-1 or coltrack[j]==-1:
                    matrix[i][j]=0
                    
