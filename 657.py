class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        a = 0;
        b = 0;
        for i in moves:
            if i == 'R':
                a = a + 1;
            elif i == 'L':
                a = a - 1;
            elif i == 'U':
                b = b + 1;
            elif i == 'D':
                b = b - 1;
        if a == 0 and b == 0:
            return True;
        else:
            return False;
