class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        curr = dummy
        curr1, curr2 = l1, l2

        while curr1 or curr2 or carry:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0
            res = v1 + v2 + carry
            carry = res // 10
            digit = res % 10
            curr.next = ListNode(digit)
            curr = curr.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None

        return dummy.next