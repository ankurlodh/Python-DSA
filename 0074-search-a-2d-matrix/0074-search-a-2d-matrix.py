class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        columns=len(matrix[0])
        low=0
        high=row*columns-1
        while(low<=high):
            mid=(low+high)//2
            i=mid // columns
            j=mid % columns
            if(matrix[i][j]==target):
                return True
            elif(matrix[i][j]<target):
                low=mid+1
            else:
                high=mid-1
        return False
        

        