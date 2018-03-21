class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = [];
        res = [0]*len(temperatures);
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i-stack[-1];
                stack.pop();
            stack.append(i);
        return res;

