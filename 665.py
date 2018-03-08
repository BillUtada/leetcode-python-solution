class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        fl = True;
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1] and fl:
                fl = False;
                if i != 0 and nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i];
                else:
                    nums[i] = nums[i+1];
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                return False;
        return True;
