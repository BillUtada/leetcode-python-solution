class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = [];
        kb = ["QWERTYUIOPqwertyuiop", "ASDFGHJKLasdfghjkl", "ZXCVBNMzxcvbnm"];
        for word in words:
            tag = 0;
            fl = True;
            for letter in word:
                if letter in kb[0] and (tag == 0 or tag == 1):
                    tag = 1;
                    continue;
                elif letter in kb[1] and (tag == 0 or tag == 2):
                    tag = 2;
                    continue;
                elif letter in kb[2] and (tag == 0 or tag == 3):
                    tag = 3;
                    continue;
                else:
                    fl = False;
                    break;
            if fl:
                res.append(word);
        return res;
