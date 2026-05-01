class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def helper(root):
            nonlocal res
            if root is None:
                return 0
            
            leftMax = max(helper(root.left), 0)
            rightMax = max(helper(root.right), 0)

            res = max(res, root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        
        helper(root)
        return res