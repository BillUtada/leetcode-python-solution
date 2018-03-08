# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.res(root, 1)[0];

    def res(self, root, dep):
        if root.right == None and root.left == None:
            return [root.val, dep];
        if root.right == None:
            return self.res(root.left, dep + 1);
        if root.left == None:
            return self.res(root.right, dep + 1);
        else:
            l = self.res(root.left, dep + 1);
            r = self.res(root.right, dep + 1);
            if l[1] < r[1]:
                return r;
            else:
                return l;
        
            
