class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def helper(root):
            nonlocal best

            if root is None:
                return 0
            
            farthestLeft, farthestRight = helper(root.left), helper(root.right)

            best = max(best, farthestLeft + farthestRight)

            return 1 + max(farthestLeft, farthestRight)
        
        helper(root)

        return best