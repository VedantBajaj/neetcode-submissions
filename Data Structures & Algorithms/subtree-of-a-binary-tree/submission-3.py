# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def compare(node1,node2):
            if not node1 and not node2:
                return True
            if node1 and node2:
                if node1.val == node2.val:
                    left = compare(node1.left,node2.left)
                    right = compare(node1.right,node2.right)
                    if right and left:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        if root and subRoot:
            ans = compare(root,subRoot)
            if ans:
                return True
            else:
                left = self.isSubtree(root.left,subRoot)
                right = self.isSubtree(root.right,subRoot)
                if left or right:
                    return True
                else:
                    return False