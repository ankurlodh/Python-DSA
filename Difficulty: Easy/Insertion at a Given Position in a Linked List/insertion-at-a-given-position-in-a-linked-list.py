'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def insertPos(self, head, pos, val):
        new_node = Node(val)

        # Insert at beginning
        if pos == 1:
            new_node.next = head
            return new_node

        temp = head

        # Move to node before position
        for i in range(pos - 2):
            temp = temp.next

        # Insert node
        new_node.next = temp.next
        temp.next = new_node

        return head
      