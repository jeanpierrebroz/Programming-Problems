class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(l1, l2, carry):
            if l1 is None and l2 is None:
                if carry:
                    return ListNode(carry, None)
                return None

            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            curr = num1 + num2 + carry

            if curr > 9:
                carry = 1
                curr %= 10
            else:
                carry = 0
            
            nxt = add(l1.next if l1 else None, l2.next if l2 else None, carry)
            
            return ListNode(curr, nxt)
            
        return add(l1, l2, 0)