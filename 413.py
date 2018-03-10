class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0;
        tmp = 1;
        for i in range(2, len(A)):
            if A[i] - A[i-1] != A[i-1] - A[i-2]:
                tmp = 1;
            else:
                res = res + tmp;
                tmp = tmp + 1;
        return res;
