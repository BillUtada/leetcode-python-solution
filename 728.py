class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right+1):
            fl = True;
            num = str(i);
            if '0' in num:
                continue;
            for dig in num:
                if i%int(dig) != 0:
                    fl = False;
                    break;
            if fl:
                res.append(i);
        return res;
