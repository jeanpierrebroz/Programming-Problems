import unittest
#for each node in graph, add all neighbors to stack. dfs uses a stack, not a queue. 

class GraphNode:
    def __init__(self, val) -> None:
        self.neighbors = []
        self.val = val
    
    def add_neighbors(self, neighbors):
        self.neighbors.extend(neighbors)

def dfs_recursive(node):
    seen = set()
    result = []
    
    def helper(node):
        seen.add(node)
        result.append(node.val)
        for neighbor in node.neighbors:
            if neighbor not in seen:
                helper(neighbor)
    
    helper(node)
    
    return result
    
def dfs_iterative(node: GraphNode):
    seen = set()
    stack = [node]
    
    result = []
        
    while stack:
        #for each element in the stack, add them as a node to search
        curr_node = stack.pop()
        
        if curr_node not in seen:
            seen.add(curr_node)
            stack.extend(reversed([n for n in curr_node.neighbors if n not in seen]))
            result.append(curr_node.val)

    
    return result
    
class DfsTests(unittest.TestCase):
    
    def test_iterative_dfs(self):
        n1 = GraphNode(1)
        n2 = GraphNode(2)
        n3 = GraphNode(3)
        n4 = GraphNode(4)
        n5 = GraphNode(5)
        
        n1.add_neighbors([n2, n3])
        n2.add_neighbors([n4, n5])
        
        n3.add_neighbors([n1, n2])
        
        result = dfs_iterative(n1)
        
        self.assertEqual([1, 2, 4, 5, 3], result)
        
    def test_recursive_dfs(self):
        n1 = GraphNode(1)
        n2 = GraphNode(2)
        n3 = GraphNode(3)
        n4 = GraphNode(4)
        n5 = GraphNode(5)
        
        n1.add_neighbors([n2, n3])
        n2.add_neighbors([n4, n5])
        
        n3.add_neighbors([n1, n2])
        
        result = dfs_recursive(n1)
        
        self.assertEqual([1, 2, 4, 5, 3], result)    
    
if __name__=="__main__":
    unittest.main()