## https://leetcode.com/problems/array-partition/

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        for i in range(len(nums)-2, -1, -2) :
            ans += nums[i]
        return ans