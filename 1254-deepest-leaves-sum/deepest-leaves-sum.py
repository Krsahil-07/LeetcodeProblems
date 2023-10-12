# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def higt(root):
            if(not(root)):
                return 0

            return max(higt(root.left),higt(root.right))+1
        mx=higt(root)
        ans=0
        q=[root]
        lvl=1
        while q:
            n=len(q)
            for i in range(n):
                f = q.pop(0)
                if(f.left) : q.append(f.left)
                if(f.right): q.append(f.right)
                if(lvl==mx):
                    ans+=f.val
            lvl+=1
        return ans
                


            
