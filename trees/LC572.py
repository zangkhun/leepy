"""
572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
# notes:  self 5/80


class SolutionT572(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t: return True
        if not s: return False
        if self.__isSameTree(s, t):
            return True
        left = self.isSubtree(s.left, t)
        right = self.isSubtree(s.right, t)
        return left or right

    def __isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q: return False
        left = self.__isSameTree(p.left, q.left)
        right = self.__isSameTree(p.right, q.right)
        return p.val == q.val and left and right
