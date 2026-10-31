# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs (node, depth):
            if not node:
                return
            if len(res)==depth:#this checks ensure tht we get the node at each level exactly one along with the other condition
                res.append(node.val)
            dfs(node.right, depth+1) # this simply does:runs the function on all the right node first then goes to left
            dfs(node.left,depth+1) 
        dfs(root,0)#function call with the parameters as mentioned in the defintion
        return res        
                

        