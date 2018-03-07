class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        res = "";
        for i in S:
            res = res + i * T.count(i);
        for t in T:
            if S.count(t) == 0:
                res = res + t;
        return res;
