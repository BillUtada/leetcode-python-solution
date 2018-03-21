class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(lambda x, y : x^y, nums);
        unique = 1;
        while(xor&unique == 0):
            unique = unique << 1;
        a = 0;
        b = 0;
        for num in nums:
            if num&unique == 0:
                a ^= num;
            else:
                b ^= num;
        return [a, b];
