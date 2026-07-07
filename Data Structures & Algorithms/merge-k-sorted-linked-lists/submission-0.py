# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into one sorted linked list.

        Args:
            lists: Array of k linked-lists, each sorted in ascending order

        Returns:
            Head of the merged sorted linked list

        Time Complexity: O(N log k) where N is total nodes, k is number of lists
        Space Complexity: O(k) for the heap
        """
        n = len(lists)
        if n == 0:
            return None

        def mergeTwoListsRecursive(
            list1: Optional[ListNode], list2: Optional[ListNode]
        ):
            if not list1:
                return list2

            if not list2:
                return list1

            if list1.val < list2.val:
                list1.next = mergeTwoListsRecursive(list1.next, list2)
                return list1
            else:
                list2.next = mergeTwoListsRecursive(list1, list2.next)
                return list2

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(mergeTwoListsRecursive(l1, l2))
            lists = merged

        return lists[-1]