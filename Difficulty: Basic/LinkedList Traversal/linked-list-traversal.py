
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    def printList(self, head):
        temp=head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
        
        