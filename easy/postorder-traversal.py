class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def helper(root):
            if root is None:
                return
            helper(root.left)
            helper(root.right)
            result.append(root.val)
        helper(root)
        return result