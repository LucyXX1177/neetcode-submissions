# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 设计一个dummy head 作为result_node的开头
        dummy=ListNode()
        result_current=dummy

        # 两个pointer指向目前的每个ListNode的开头
        current1=list1
        current2=list2 

        while current1 != None and current2 != None :
            print(dummy.next)
            if current1.val<current2.val or current1.val==current2.val:
               result_current.next=current1
               current1=current1.next 
               result_current=result_current.next
               
            else:
               result_current.next=current2
               current2=current2.next 
               result_current=result_current.next
        
        # 这里没有想明白，如果有剩余的没有插入的部分 ==>需要next
        if current1 is not None:
            result_current.next=current1
        else:
            result_current.next=current2
        return dummy.next
                