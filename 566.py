class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ls = [];
        if r*c != len(nums)*len(nums[0]):
            return nums;
        for i in range(0, len(nums)):
            for j in range(0, len(nums[0])):
                ls.append(nums[i][j]);
        res = [];
        for i in range(0, r):
            tmp = [];
            for j in range(0, c):
                tmp.append(ls[i*c+j]);
            res.append(tmp);
        return res;
