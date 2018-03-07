class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = [];
        head = 0;
        tail = 1;
        if len(S) == 1:
            res.append(1);
            return res;
        while tail <= len(S):
            pt = head;
            while pt != tail:
                f = S.rfind(S[pt], tail, len(S));
                if f != -1:
                    tail = f+1;
                pt = pt + 1;
            res.append(tail-head);
            head = tail;
            tail = head + 1;
        return res;
                    
