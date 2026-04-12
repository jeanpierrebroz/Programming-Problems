class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def helper(root: Optional[TreeNode]) -> None:
            if root is None:
                return
            result.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        
        return result