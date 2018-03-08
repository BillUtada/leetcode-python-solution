class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [];
        res.append(0);
        for i in range(1, num+1):
            res.append(res[i/2] + i%2);
        return res;
