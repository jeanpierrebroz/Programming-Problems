# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #at the bottom of the leaf you have a complete path
        result = 0
        def dfs(root, num):
            nonlocal result

            if not root:
                return
            
            num = num * 10 + root.val

            if not root.left and not root.right:
                result += num
            
            dfs(root.left, num)
            dfs(root.right, num)

            return

        dfs(root, 0)
        return result