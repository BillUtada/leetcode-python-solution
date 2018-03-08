class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        nge = {};
        stack = [];
        for num in nums:
            while stack and stack[-1] < num:
                nge[stack.pop()] = num;
            stack.append(num);
        return [nge.get(n, -1) for n in findNums];
