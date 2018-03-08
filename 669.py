# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root == None:
            return None;
        if root.val < L:
            root = root.right;
            return self.trimBST(root, L, R);
        elif root.val > R:
            root = root.left;
            return self.trimBST(root, L, R);
        else:
            root.left = self.trimBST(root.left, L, R);
            root.right = self.trimBST(root.right, L, R);
            return root;
