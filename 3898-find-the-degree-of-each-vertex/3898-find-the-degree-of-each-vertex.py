import numpy as np

class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        ans = np.sum(matrix, axis=0).tolist()

        return ans