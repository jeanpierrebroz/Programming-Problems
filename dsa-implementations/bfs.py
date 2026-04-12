import unittest
from collections import deque

class GraphNode:
    def __init__(self, val) -> None:
        self.neighbors = []
        self.val = val
    
    def add_neighbors(self, neighbors):
        self.neighbors.extend(neighbors)
    
def bfs(node: GraphNode):
    seen = set()
    
    q = deque()
    
    q.append(node)
    
    result = []
        
    while q:
        curr_node = q.popleft()
        
        seen.add(curr_node)
        
        for neighbor in curr_node.neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                q.append(neighbor)
                
        result.append(curr_node.val)

    
    return result
    
class BfsTests(unittest.TestCase):
    
    def test_iterative_dfs(self):
        n1 = GraphNode(1)
        n2 = GraphNode(2)
        n3 = GraphNode(3)
        n4 = GraphNode(4)
        n5 = GraphNode(5)
        
        n1.add_neighbors([n2, n3])
        n2.add_neighbors([n4, n5])
        
        n3.add_neighbors([n1, n2])
        
        result = bfs(n1)
        
        self.assertEqual([1, 2, 3, 4, 5], result)

if __name__=="__main__":
    unittest.main()