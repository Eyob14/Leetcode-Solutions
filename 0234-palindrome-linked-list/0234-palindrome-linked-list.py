# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverser(idx):
            pre = None
            while idx:
                next_ = idx.next
                idx.next = pre
                pre = idx
                idx = next_
            return pre
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        reverse = reverser(slow)
        
        while reverse:
            if reverse.val != head.val:
                return False
            reverse = reverse.next
            head = head.next
        return True
        