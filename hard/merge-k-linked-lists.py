# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        dummy = ListNode(None, None)
        curr = dummy
        for l in lists:
            if l:
                heapq.heappush(heap, l)
        
        while heap:
            nxt = heapq.heappop(heap)
            new_node = nxt.next
            if new_node:
                heapq.heappush(heap, new_node)
            
            curr.next = nxt
            nxt.next = None
            curr = curr.next
        
        return dummy.next
