# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ant = dict()
        if root:
            ant[root.val] = [root]
        def dfs(node,arr1):
            nonlocal ant
            if node:
                if node.left:
                    arr1.append(node)
                    dfs(node.left,arr1)
                    ant[node.left.val]= arr1[::]
                    arr1.pop()
                if node.right:
                    arr1.append(node)
                    dfs(node.right,arr1)
                    ant[node.right.val]= arr1[::]
                    arr1.pop()
        dfs(root,[])
        a1,a2 = ant[p.val]+[p],ant[q.val]+[q]
        ans = None
        for i in a1:
            for j in a2:
                # print(i.val,j.val)
                if i.val == j.val:
                    # print(i.val,j.val)
                    ans = i
        return ans

