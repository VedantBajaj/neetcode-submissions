# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def compare_node(node1,node2):
            # print(node1.val,node2.val)
            if not node1 and not node2:
                return True
            if node1 and node2:
                if (node1.val == node2.val):
                    return True
                else:
                    return False
            else:
                return False

        def dfs(node1,node2):
            if not node1 and not node2:
                return True
            if node1 and node2:
                ans = compare_node(node1,node2)
                left = True
                right = True
                if ans:
                    left = dfs(node1.left,node2.left)
                    right = dfs(node1.right,node2.right)
                return ans and left and right
            else:
                return False
        ret = dfs(p,q)
        return ret
            