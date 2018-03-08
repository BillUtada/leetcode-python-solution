class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        s = [int(ops[0])];
        for i in range(1, len(ops)):
            if ops[i] == 'D':
                s.append(s[len(s)-1] * 2);
            elif ops[i] == '+':
                s.append(s[len(s)-1] + s[len(s)-2]);
            elif ops[i] == 'C':
                del s[len(s)-1];
            else:
                s.append(int(ops[i]));
        res = 0;
        for i in s:
            res = res + i;
        return res;
