# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next # initiate slow and fast pointers to find mid
        
        while fast and fast.next: # find mid
            slow = slow.next
            fast = fast.next.next
        
        prev = None # initiate head of the second reversed part
        curr = slow.next # initiate pointer to reverse second part
        slow.next = None # remove pointer to the second part
        
        while curr: # reverse second part
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        first, second = head, prev
        while second: # join 2 parts together
            next1, next2 = first.next, second.next
            first.next = second
            second.next = next1
            first, second = next1, next2