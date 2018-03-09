class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n%4 == 0 or n%4 == 3:
            return False;
        elif n%4 == 1:
            t = 1;
        else:
            t = 2;
        while n != 0:
            if n%4 != t:
                return False;
            n = n/4;
        return True;
