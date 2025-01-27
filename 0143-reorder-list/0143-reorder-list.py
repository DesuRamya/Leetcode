# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev,cur=None,slow.next
        slow.next=None
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        node1,node2=head,prev
        while node2:
            temp1,temp2=node1.next,node2.next
            node1.next=node2
            node2.next=temp1
            node1,node2=temp1,temp2