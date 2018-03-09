# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = [];
        que = [];
        if root != None:
            que.append(root);
        while que:
            res.append(max([node.val for node in que]));
            tmpq = [];
            for node in que:
                if node.left != None:
                    tmpq.append(node.left);
                if node.right != None:
                    tmpq.append(node.right);
            que = tmpq;
        return res;
