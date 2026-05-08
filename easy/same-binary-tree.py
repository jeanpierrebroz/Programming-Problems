class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is None):
            return True
        
        elif (p is None and q) or (q is None and p) or (p.val != q.val):
            return False
        

        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)            
        