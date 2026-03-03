class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while  True:
            if root is None or root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        
        return None
