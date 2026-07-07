# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse the nodes of the list k at a time.

        Args:
            head: Head of the linked list
            k: Number of nodes to reverse in each group

        Returns:
            Head of the modified list

        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(1) for iterative, O(n/k) for recursive
        """
        dummy = ListNode()
        dummy.next = head
        prev_segment_end = dummy

        while True:
            end = self.findKth(prev_segment_end, k)
            if not end:
                return dummy.next

            next_segment_head = end.next
            segment_head = prev_segment_end.next
            self.reverseSegment(segment_head, next_segment_head)
            segment_head.next = next_segment_head
            prev_segment_end.next = end
            prev_segment_end = segment_head

    def findKth(self, node: Optional[ListNode], k: int):
        while node and k > 0:
            node = node.next
            k -= 1

        return node if k == 0 else None

    def reverseSegment(self, curr: ListNode, next_segment: ListNode):
        prev = None
        while curr != next_segment:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
        