## https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums)) - 1 if 0 in nums else len(set(nums))