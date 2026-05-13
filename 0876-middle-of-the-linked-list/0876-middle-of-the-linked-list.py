# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        temp=head
        while temp:
            temp=temp.next
            c=c+1
        mid=c//2
        temp=head
        for i in range(mid):
            temp=temp.next
        return temp
