'''
Definition for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        # code here
        temp=head
        count=0
        while temp is not None:
            temp=temp.next
            count=count+1
        return count