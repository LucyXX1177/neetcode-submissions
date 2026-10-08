# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# idea: 使用两次reverseLink: 
# 先reverse linked list : 找到这个顺着的n-th node
# 找到这个nodes删除后
# 再重新reverse 回来

# 怎么记住
def reverselink(head: Optional[ListNode])-> Optional[ListNode]:
    prev=None
    curr=head
    while curr!=None:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp 
    return prev

        


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reverse_link=reverselink(head)
        
        cnt=1
        pointer=reverse_link
        prev = None
        # 这里还需要再优化就是不遍历全部找到吗
        while cnt!=n:
            prev=pointer
            pointer=pointer.next
            cnt+=1

        # 删除掉目前的current_pointer
        if prev is None:
            # 删除 reverse 后的第一个 node
            reverse_link = pointer.next
        else:
 
            temp=pointer.next 
            prev.next=temp

        reverse_back=reverselink(reverse_link)
        return reverse_back



        

            

