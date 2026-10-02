import numpy as np

class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        ans = [sum(row) for row in matrix]

        return ans