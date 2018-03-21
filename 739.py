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

	'''
        res = [0]*len(temperatures);
        dic = {};
        for i in range(len(temperatures))[::-1]:
            nearest = len(temperatures);
            for temp in range(temperatures[i]+1, 101):
                if temp in dic and dic[temp] < nearest:
                    nearest = dic[temp];
            if nearest != len(temperatures):
                res[i] = nearest-i;
            dic[temperatures[i]] = i;
        return res;
        '''
