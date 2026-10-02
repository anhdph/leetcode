class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        prd = 0

        for i, letter in enumerate(s):

            apb_idx = 27 - (ord(letter.lower()) - ord('a') + 1)
            print(apb_idx)
            print(i)

            prd += apb_idx * (i+1)

        return prd