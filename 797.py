class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]] 
        :rtype: List[List[int]]
        """
        return self.findpath(graph = graph, start = 0);

    def findpath(self, graph, start):
        if start == len(graph)-1:
            return [[start]];
        if len(graph[start]) == 0:
            return [];
        ret = [];
        for node in graph[start]:
            tmp = self.findpath(graph, node);
            for path in tmp:
                path.insert(0, start);
                ret.append(path);
        return ret;
            
