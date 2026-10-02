import numpy as np

class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        ans = [0] * len(matrix[0])

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                ans[i] += matrix[j][i]

        return ans