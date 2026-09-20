# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_reversed = self.reverseLinkedList(l1)
        l2_reversed = self.reverseLinkedList(l2)
        num1 = 0 
        cur1 =l1_reversed
        while cur1:
            num1 = num1*10 + cur1.val
            cur1 = cur1.next
        num2 = 0
        cur2 = l2_reversed
        while cur2:
            num2= num2*10 + cur2.val
            cur2 = cur2.next
        total = num1 + num2
        if total == 0 :
            return ListNode(0)
        dummy = ListNode(0)
        cur = dummy

        while total:
            digit = total % 10
            cur.next = ListNode(digit)
            cur = cur.next

            total = total // 10

        return dummy.next

    def reverseLinkedList(self, head):
        dummy_head = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = dummy_head
            dummy_head = cur
            cur = temp
        return dummy_head
