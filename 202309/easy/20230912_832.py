## https://leetcode.com/problems/flipping-an-image/

class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in image : i.reverse()
        for i in image :
            for j in range(len(i)) :
                if i[j] == 0 : i[j] = 1
                else : i[j] = 0
        return image