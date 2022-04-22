'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Author: Imanol López
Time Complexity: O(n)
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        output_list = ListNode(0) 
        head = output_list

        while( list1 != None and list2 != None ):
        
            if( list1.val <= list2.val ):
                output_list.next = list1
                list1 = list1.next
            else:
                output_list.next = list2
                list2 = list2.next

            output_list = output_list.next

        output_list.next = list1 or list2
        
        return head.next