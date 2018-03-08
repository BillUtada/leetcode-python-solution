class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [];
        s = sorted(people, self.ccmp);
        for man in s:
            res.insert(man[1], man);
        return res;
    
    def ccmp(self, a, b):
        if a[0] < b[0]:
            return 1;
        elif a[0] > b[0]:
            return -1;
        elif a[1] < b[1]:
            return -1;
        else:
            return 1;
