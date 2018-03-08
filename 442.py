class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [];
        for i in range(0, len(nums)):
            if nums[i] > 0:
                if nums[nums[i]-1] < 0:
                    res.append(nums[i]);
                else:
                    nums[nums[i]-1] = -nums[nums[i]-1];
            else:
                if nums[-nums[i]-1] < 0:
                    res.append(-nums[i]);
                else:
                    nums[-nums[i]-1] = -nums[-nums[i]-1];
        return res;
