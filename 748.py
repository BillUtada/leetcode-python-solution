class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        checkmsg = ''.join([licensePlate[i].lower() for i in range(len(licensePlate)) if licensePlate[i].isalpha()]);
        ls = list(checkmsg);
        ls.sort();
        checkmsg = ''.join(ls);
        words.sort(self.cmp);
        # find checkmsg in words
        for word in words:
            fl = True
            for letter in checkmsg:
                if word.count(letter) < checkmsg.count(letter):
                    fl = False
                    break;
            if fl:
                return word;
    
    def cmp(self, s1, s2):
        if len(s1) > len(s2):
            return 1;
        elif len(s1) < len(s2):
            return -1;
        else:    
            return 0;
