# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Add two numbers represented as linked lists in reverse order.

        Approach:
        1. Traverse both lists simultaneously
        2. Add corresponding digits plus carry
        3. Create new node with sum % 10
        4. Update carry as sum // 10
        5. Handle remaining carry at the end

        Time Complexity: O(max(m, n)) where m, n are lengths of lists
        Space Complexity: O(max(m, n)) for the result list
        """

        def add(
            l1: Optional[ListNode], l2: Optional[ListNode], carry: int
        ) -> Optional[ListNode]:
            if not l1 and not l2 and carry == 0:
                return None

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            val = l1_val + l2_val + carry
            carry = val // 10
            val %= 10

            next_node = add(l1.next if l1 else None, l2.next if l2 else None, carry)
            return ListNode(val, next_node)

        return add(l1, l2, 0)