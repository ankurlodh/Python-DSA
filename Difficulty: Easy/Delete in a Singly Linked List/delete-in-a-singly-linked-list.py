'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        #code here
        if x==1:
            return head.next
        temp = head

        # Move to node before position
        for i in range(x - 2):
            temp = temp.next

        # Delete node
        temp.next = temp.next.next

        return head
        
