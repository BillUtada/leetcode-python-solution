class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = len(s);
        dp = [[0 for x in range(len(s))] for y in range(len(s))];
        for i in range(len(s)):
            dp[i][i] = True;
        for j in range(1, len(s)):
            for i in range(j)[::-1]:
                dp[i][j] = s[i] == s[j] and (i == j-1 or dp[i+1][j-1]);
                if dp[i][j]:
                    res = res + 1;
        return res;
