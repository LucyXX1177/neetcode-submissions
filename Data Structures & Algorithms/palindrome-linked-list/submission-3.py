# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 解法1：保留所有走过的记录
# 只能想到暴力解法 没法做到space complexity O（1）
# result_stack=[]
# curr=head
# while curr is not None:
    
#     result_stack.append(curr.val)
#     curr=curr.next

# return result_stack==result_stack[::-1]

# 解法2：快慢指针找需要开始反转的midpoint

class Solution:
    
    #还是不熟悉这个这么写
    #3. Reverse Linked List
    def reverselink(self,head:Optional[ListNode]):
        prev=None
        curr=head
        while curr!=None:
            temp=curr.next 
            curr.next=prev
            prev=curr
            curr=temp
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        fast_pointer=head # 永远要走两步 （必须保证 fast.next 不是None）
        slow_pointer=head 
        
        # 防止fast_pointer.next.next报错 
        while fast_pointer != None and fast_pointer.next!=None:
            fast_pointer=fast_pointer.next.next
            slow_pointer=slow_pointer.next 

        
        midpoint=slow_pointer 
        reverse_mid_link=self.reverselink(midpoint)
        
        while reverse_mid_link:
            if reverse_mid_link.val!=head.val:
                    return False 
            else:
                reverse_mid_link=reverse_mid_link.next 
                head=head.next 
        
        return True

            






