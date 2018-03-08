class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        dic = {};
        for i in candies:
            if i in dic:
                dic[i] = dic[i] + 1;
            else:
                dic[i] = 1;
        if len(candies)/2 > len(dic):
            return len(dic);
        else:
            return len(candies)/2;
            
