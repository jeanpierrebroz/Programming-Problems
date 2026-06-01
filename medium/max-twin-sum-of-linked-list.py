class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #how can we efficiently calculate the twin sums?
        #reverse middle, then iterate
        result = -1

        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        h2 = prev
        h1 = slow

        while h1 and h2:
            result = max(result, h1.val + h2.val)
            h1 = h1.next
            h2 = h2.next
        return result