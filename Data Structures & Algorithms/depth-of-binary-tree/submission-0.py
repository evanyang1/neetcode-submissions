# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def helper(root, dep):
            nonlocal depth  # Use nonlocal instead of global for nested function
            if not root:
                return
            depth = max(depth, dep)
            helper(root.left, dep+1)
            helper(root.right, dep+1)
        helper(root, 1)
        return depth
