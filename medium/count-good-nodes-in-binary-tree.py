class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #subproblem: given a node and the previous max, increment if the nodes val is leq
        result = 0
        def helper(node, maxVal):
            nonlocal result
            if node is None:
                return 
            
            if node.val >= maxVal:
                maxVal = node.val
                result += 1
            
            helper(node.left, maxVal)
            helper(node.right, maxVal)
        
        helper(root, -101)
        return result