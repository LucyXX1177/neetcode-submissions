# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 方法2： 使用两个指针slow and fast慢走和先走指针
        # 因为是倒叙数第几个，所以就让fast多走几步
        
        cnt=0
        fast=head
        slow=head

        while cnt!=n-1:
            cnt+=1
            fast=fast.next
       
        prev = None
        while fast.next !=None:
            fast=fast.next
            prev=slow 
            slow=slow.next

        # 目前的slow就是想要找到的position
        temp=slow.next 
        if prev:
            prev.next=temp
        else:
            head = head.next
        return head
