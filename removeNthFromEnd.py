# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l=[]
        if n==0:
            return head
        else:
            while head != None:
                l.append(head.val)
                head=head.next
        
        l=l[::-1]
        l=l[:n-1]+l[n:]
        ls=None
        for i in l:
            new_node = ListNode(i)
            new_node.next = ls
            ls = new_node
         
        return ls   
