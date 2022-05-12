# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1=[]
        num2=[]
        printval = l1
        while printval is not None:
            num1.append(printval.val)
            printval=printval.next
        printval1 = l2
        while printval1 is not None:
            num2.append(printval1.val)
            printval1=printval1.next
        x=''
        y=''
        num1=num1[::-1]
        num2=num2[::-1]
        for i in num1:
            x=x+str(i)
        for j in num2:
            y=y+str(j)
            
        num3 = int(x)
        num4 = int(y)
        
        res = str(num3+num4)
        res=res[::-1]
        print(res)
        head = ListNode(int(res[0]))
        tail=head
        e=1
        while e < len(res):
            tail.next = ListNode(int(res[e]))
            tail = tail.next
            e=e+1
        return head
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        