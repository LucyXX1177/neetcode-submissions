# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 这题思路很清晰
# 就是遍历成为string--> 直接加起来
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr1=l1
        curr2=l2
        string1=""
        
        string2=""
        
        while curr1:
            string1=str(curr1.val)+string1
            curr1=curr1.next 



        while curr2:
            string2=str(curr2.val)+string2
            curr2=curr2.next 
            
        print(int(string1))
        
        str_sum1= str(int(string1)+int((string2)))
        reverse_str_sum1 = str_sum1[::-1]

        head=ListNode()
        curr=head 
        for i in range(len(reverse_str_sum1)):
            
            temp=ListNode(int(reverse_str_sum1[i]))
            curr.next=temp
            curr=temp
        return head.next 

            

        