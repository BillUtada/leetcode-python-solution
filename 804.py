class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letters = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
        dic = {};
        res = 0;
        for word in words:
            mose = '';
            for letter in word:
                mose += letters[ord(letter)-ord('a')];
            if mose not in dic:
                dic[mose] = None;
                res += 1;
        return res;
