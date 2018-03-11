class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0;
        tmp = 0;
        for n in nums:
            tmp = (tmp + n) * n;
            res = max(res, tmp);
        return res;
                
