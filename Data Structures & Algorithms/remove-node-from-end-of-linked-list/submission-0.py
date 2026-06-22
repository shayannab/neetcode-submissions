class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        # move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # move both together until fast hits None
        while fast:
            slow = slow.next
            fast = fast.next

        # remove the node after slow
        slow.next = slow.next.next

        return dummy.next