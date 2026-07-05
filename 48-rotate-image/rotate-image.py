class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        
        for i in range(0,n-1):
            for j in range(i+1,n):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        
        for i in matrix:
            i.reverse()
        