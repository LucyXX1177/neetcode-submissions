# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 只能想到暴力解法 没法做到space complexity O（1）
        result_stack=[]
        curr=head
        while curr is not None:
           
            result_stack.append(curr.val)
            curr=curr.next

        return result_stack==result_stack[::-1]