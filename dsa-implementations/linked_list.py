import unittest

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None
        

def traverse_and_apply(node, x):
    if node is None:
        return
    x(node)
    traverse_and_apply(node.next, x)
    
def remove_node(head, val: int):
    prev, curr, front = None, head, head
    
    
    while curr is not None:
        if curr.val == val:
            #if prev is none, the head is the node to remove
            if prev is None:
                front = head.next
                head.next = None
            else:
                prev.next = curr.next
            return front
        prev = curr
        curr = curr.next
    
    return front
    
class LinkedListTests(unittest.TestCase):
    
    def test_traverse_and_apply(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n1.next = n2
        n2.next = n3
        
        def mult(node):
            node.val *= 2
        traverse_and_apply(n1, mult)
        
        self.assertEqual(n1.val, 2)
        self.assertEqual(n2.val, 4)
        self.assertEqual(n3.val, 6)
        
    def test_remove_on_head_with_val_returns_second(self):
         n1 = Node(1)
         n2 = Node(2)
         n3 = Node(3)
         n1.next = n2
         n2.next = n3
         
         head = remove_node(n1, 1)
         
         self.assertEqual(head, n2)
         
    def test_remove_on_middle(self):
         n1 = Node(1)
         n2 = Node(2)
         n3 = Node(3)
         n1.next = n2
         n2.next = n3
         
         head = remove_node(n1, 2)
         
         self.assertEqual(n1.next, n3)
    def test_remove_on_end(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n1.next = n2
        n2.next = n3
        
        head = remove_node(n1, 3)
        
        self.assertEqual(n2.next, None)

if __name__ == "__main__":
    unittest.main()