# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue;
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = [];
        que = [root];
        while que:
            res.append(1.0 * sum([n.val for n in que])/len(que));
            tmpq = [];
            for node in que:
                if node.left != None:
                    tmpq.append(node.left);
                if node.right != None:
                    tmpq.append(node.right);
                que = tmpq;
        return res;
