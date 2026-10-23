# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def max_depth(root):
            if root is None:
                return 0
            else:
                return 1 + max(max_depth(root.left),max_depth(root.right))
        def Bal_val(root):
            return abs(max_depth(root.left) - max_depth(root.right))

        def isBal(root):
            if root is None:
                return True
            if Bal_val(root) > 1:
                return False
            else:
                return isBal(root.left) and isBal(root.right)

        return isBal(root)