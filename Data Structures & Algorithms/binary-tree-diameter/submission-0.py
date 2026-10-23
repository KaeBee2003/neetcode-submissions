# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_depth(root):
            if root is None:
                return 0
            else:
                return 1 + max(max_depth(root.left), max_depth(root.right))
        max_dia = 0
        def dia(root):
            nonlocal max_dia
            if root is None:
                return 0
            else:
                max_dia = max_depth(root.left) + max_depth(root.right)
                return max(max_dia,dia(root.left),dia(root.right))
        return dia(root)