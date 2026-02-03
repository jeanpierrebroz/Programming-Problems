class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []

        while head is not None:
            arr.append(head.val)
            head = head.next
        
        max_sum = -1
        n = len(arr)
        
        for i in range(n//2):
            max_sum = max(max_sum, arr[i] + arr[n-1-i])

        return max_sum