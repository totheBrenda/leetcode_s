## https://leetcode.com/problems/keep-multiplying-found-values-by-two/

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums : original *= 2
        return original