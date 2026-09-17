# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 每次想要反转箭头的同时，需要用temp先记录original的next
        # 先保存后路，再改箭头
        # head先找到ListNode的第一位
        prev,curr=None,head

        while curr:
            temp=curr.next 
            # 例如[Node(1),Node(2),Node(3),Node(4)...]
            # 这一步的时候变成了两个断开的Link：
            # 1) [None <- Node(1)] 
            # 2) [Node(2)->Node(3)-> Node(4)...]
            curr.next=prev
            prev=curr
            curr=temp
        
        # return [Node(4) -> Node(3) -> Node(2) -> Node(1) ->None]
        return prev