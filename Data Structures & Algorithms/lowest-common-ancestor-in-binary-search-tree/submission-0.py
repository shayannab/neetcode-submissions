# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr=root
        while curr:
            if not curr:
                return 0
            if p and q and curr.val>=min(p.val, q.val) and curr.val<=max(p.val,q.val):
                return curr
            elif p and q and curr.val>=min(p.val, q.val) and curr.val>=max(p.val,q.val):  
                curr=curr.left
            else:
                curr=curr.right
        return 0             