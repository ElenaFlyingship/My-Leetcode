# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        slow = fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        current = slow
        prev = None

        while current is not None:
            next_node = current.next
            current.next = prev
            prev=current
            current = next_node

        right  = prev
        left = head

        while right is not None:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next    

        return True    

        
       
        

