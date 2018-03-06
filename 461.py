class Solution(object):
    def hammingDistance(self, x, y):
        res = 0;
        while not (x == 0 and y == 0):
            if not x%2 == y%2:
                res = res + 1;
            x = x/2;
            y = y/2;
        return res;
