class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        cur = 0;
        line = 1;
        for letter in S:
            oc = widths[ord(letter)-ord('a')]
            if cur + oc <= 100:
                cur += oc;
            else:
                line += 1;
                cur = oc;
        return [line, cur];
