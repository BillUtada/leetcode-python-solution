class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        originnums = nums[:]
        nums.sort()
        pt1 = 0
        pt2 = len(nums)-1
        (res1, res2) = (nums[pt1], nums[pt2])
        while(True):
            if nums[pt1]+nums[pt2] < target:
                pt1 += 1
                res1 = nums[pt1]
            elif nums[pt1]+nums[pt2] > target:
                pt2 -= 1
                res2 = nums[pt2]
            else:
                break;
        return [originnums.index(res1), len(nums)-originnums[::-1].index(res2)-1]
