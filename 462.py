class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0;
        des = nums[len(nums)/2]
        for num in nums:
            res += abs(num-des);
        return res;
