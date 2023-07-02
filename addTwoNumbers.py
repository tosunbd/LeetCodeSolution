# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0
        
        while l1 or l2:
            sum = carry
            
            if l1:
                sum += l1.val
                l1 = l1.next
            
            if l2:
                sum += l2.val
                l2 = l2.next
            
            carry = sum // 10
            sum %= 10
            
            current.next = ListNode(sum)
            current = current.next
        
        if carry != 0:
            current.next = ListNode(carry)
        
        return dummyHead.next