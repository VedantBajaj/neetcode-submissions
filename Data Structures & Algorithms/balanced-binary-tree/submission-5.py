# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        var = True
        def dfs(node,ans):
            nonlocal var
            if node:
                left = 0
                right = 0
                if node.left:
                    left = dfs(node.left,ans+1)
                if node.right:
                    right = dfs(node.right,ans+1)
                if abs(left-right)<=1 and var:
                    return 1+max(left,right)
                else:
                    var=False
                    return 1+max(left,right)
        dfs(root,0)
        return var