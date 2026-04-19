class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def helper(root):
            if root is None:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)
            
            if abs(left - right) > 1:
                self.balanced = False
                
            return 1 + max(left, right)
        
        helper(root)

        return self.balanced