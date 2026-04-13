# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        count=0
        temp=head
        while(temp):
            count+=1
            temp=temp.next
        pos=count-n
        temp2=head
        if pos==0:
            return head.next
        while(pos>1):
            temp2=temp2.next
            pos-=1
        temp2.next=temp2.next.next
        return head
