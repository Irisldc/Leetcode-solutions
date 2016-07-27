def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1=[]
        list2=[]
        merged_list=[]
        while l1!=None:
            list1.append(l1.val)
            l1=l1.next
        while l2!=None:
            list2.append(l2.val)
            l2=l2.next
        merged_list=list1+list2
        merged_list=sorted(merged_list)
        print merged_list
        merged_reorder_list=merged_list[::-1]

        previous_ls=None
        for i in merged_reorder_list:
            temp=ListNode(i)
            temp.next=previous_ls
            previous_ls=temp
        
        return previous_ls
