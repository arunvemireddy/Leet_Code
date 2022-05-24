# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head==None:
            return head
        l = set()
        while head!=None:
            val = head.val
            head = head.next
            l.add(val)
        res=list(l)
        res.sort()
        print(res)
        head = ListNode(res[0])
        tail = head
        for i in range(1,len(res)):
            tail.next=ListNode(res[i])
            tail=tail.next
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        