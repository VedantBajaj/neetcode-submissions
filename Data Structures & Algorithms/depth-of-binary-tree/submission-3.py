# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node,ans):
            if node:
                left = 0
                right = 0
                if node.left:
                    left = dfs(node.left,ans+1)
                if node.right:
                    right = dfs(node.right,ans+1)
                return 1+max(left,right)
            else:
                return 0
        ans = dfs(root,0)
        return ans