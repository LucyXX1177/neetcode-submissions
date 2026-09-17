# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 每次想要反转箭头的同时，需要用temp先记录original的next
        # 先保存后路，再改箭头
        prev,curr=None,head

        while curr:
            temp=curr.next 
            curr.next=prev
            prev=curr
            curr=temp
        
        return prev