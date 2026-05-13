'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        slow=head
        fast=head
        count=1
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                temp=slow.next
                while slow!=temp:
                    count+=1
                    temp=temp.next
                return count
        return 0
        
        