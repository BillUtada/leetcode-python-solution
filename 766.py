class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(0, len(matrix)-1):
            for j in range(0, len(matrix[i])-1):
                if matrix[i+1][j+1] != matrix[i][j]:
                    return False;
        return True;
