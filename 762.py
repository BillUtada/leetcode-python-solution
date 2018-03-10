class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0;
        prime = [2, 3, 5, 7, 11, 13, 17, 19];
        for n in range(L, R+1):
            if bin(n)[2:].count('1') in prime:
                res = res + 1;
        return res;
