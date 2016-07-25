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
        #reverse a list
        l=l[::-1]
        #delete the nth element from the begining
        l=l[:n-1]+l[n:]
        #define a linkedlist to store the previews linkedlist
        previews_ls=None
        for i in l:
            #initialize a new ListNode
            new_node = ListNode(i)
            #assign previews linkedlist to the next of the current node
            new_node.next = previews_ls
            #update the previews linkedlist
            previews_ls = new_node
         
        return ls   
