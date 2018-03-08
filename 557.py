class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = "";
        ls = s.split(' ');
        for word in ls:
            res = res + word[::-1] + " ";
        res = res[0: len(res)-1];
        return res;
