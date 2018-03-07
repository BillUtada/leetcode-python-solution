class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0;
        nums.sort()
        for i in range(0, len(nums)/2):
            res += nums[i*2];
        return res;
