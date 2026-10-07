# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# helper function 1 
def fast_slow_middle(head:Optional[ListNode]) -> None:
    fast_pointer=head 
    slow_pointer=head 
    while fast_pointer != None and fast_pointer.next!=None:
        fast_pointer=fast_pointer.next.next
        slow_pointer=slow_pointer.next
    return slow_pointer 

# helper function 2 
def reverselink(head: Optional[ListNode]):
    prev = None
    curr = head 
    
    while curr != None:
        temp = curr.next      # 保存原来的下一个
        curr.next = prev      # 当前节点反过来指向前一个
        prev = curr           # prev 前进
        curr = temp           # curr 前进
        
    return prev

# helper function 3 
def mergeTwoLinkedList(head1: Optional[ListNode],
                       head2: Optional[ListNode]):
    pointer1 = head1
    pointer2 = head2

    while pointer2 != None:
        # 先保存原来的 next
        temp1 = pointer1.next
        temp2 = pointer2.next

        # 交替连接
        pointer1.next = pointer2
        pointer2.next = temp1

        # 两个 pointer 向后移动
        pointer1 = temp1
        pointer2 = temp2

    return head1


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 暂时的思路是能不能中间劈开然后 得到list 1 和 list 2 (这个需要转一下顺序从后往前)
        # 找中点的思路与这个类似（Palindrome Linked List）使用fast and slow pointer 
        # 这里不能用len()因为head本身就没有长度
        middle=fast_slow_middle(head)
        # 只要前面的一半 (从head出发)
        second_half = middle.next
        middle.next =None 
        reverse_half=reverselink(second_half)
        mergeTwoLinkedList(head,reverse_half)
        


        


        




        
            


        

