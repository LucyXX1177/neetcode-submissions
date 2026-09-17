# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #快慢指针：
        #如果有cycle，必然slow和faster都会进入cycle，
        # 追及问题里面faster一定会更早进入cycle，同时会追逐到slow

        slow_pointer=head 
        fast_pointer=head

        while fast_pointer !=None and fast_pointer.next!=None:
            
            slow_pointer=slow_pointer.next 
            fast_pointer=fast_pointer.next.next 
            if slow_pointer == fast_pointer:
                return True
            
        return False 
