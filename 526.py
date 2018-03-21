class Solution(object):
    def __init__(self):
        self.res = 0;
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        visit = [False]*N;
        self.arrange(N, visit);
        return self.res;
    
    def arrange(self, already, visit):
        N = len(visit);
        if already == 0:
            self.res += 1;
        for i in range(N):
            if not visit[i] and (already%(i+1) == 0 or (i+1)%already == 0):
                visit[i] = True;
                self.arrange(already-1, visit);
                visit[i] = False;
                
