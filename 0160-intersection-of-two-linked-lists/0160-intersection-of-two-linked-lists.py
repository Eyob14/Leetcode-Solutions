# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l_1, l_2 = headA, headB
        
        while l_1 != l_2:
            l_1 = l_1.next if l_1 else headB
            l_2 = l_2.next if l_2 else headA
        return l_1
        