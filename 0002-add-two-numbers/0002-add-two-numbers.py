# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:  
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        string1 = ''
        string2 = ''
        res = ListNode()
        final = res
        while curr1:
            string1 += str(curr1.val)
            curr1 = curr1.next
        while curr2:
            string2 += str(curr2.val)
            curr2 = curr2.next
        string1 = string1[::-1]
        string2 = string2[::-1]
        string1 = int(string1) + int(string2)
        string1 = str(string1)[::-1]
        for i in string1:
            final.next = ListNode(val=int(i))
            final = final.next
        return res.next
        



        